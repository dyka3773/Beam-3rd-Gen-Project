import eBUS as eb
import logging
import numpy as np
import time
import os
from datetime import datetime

import Camera.lib.PvSampleUtils as psu

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)

BUFFER_COUNT = 16

opencv_is_available = True
try:
    # Detect if OpenCV is available
    import cv2
    opencv_version = cv2.__version__  # type: ignore
except:
    opencv_is_available = False
    logging.warn(
        "Warning: This sample requires python3-opencv to display a window")
    raise ImportError("python3-opencv is not installed")


def connect_to_device(connection_ID: str) -> eb.PvDevice:
    """Connect to the GigE Vision or USB3 Vision device

    Args:
        connection_ID (str): The ID of the device to connect to

    Returns:
        eb.PvDevice: The device object
    """
    logging.info("Connecting to device.")
    result, device = eb.PvDevice.CreateAndConnect(connection_ID)
    if device == None:
        logging.error(
            f"Unable to connect to device: {result.GetCodeString()} ({result.GetDescription()})")
    return device


def open_stream(connection_ID: str) -> eb.PvStream:
    """Open stream from the GigE Vision or USB3 Vision device

    Args:
        connection_ID (str): The ID of the device to connect to

    Returns:
        eb.PvStream: The stream object
    """
    logging.info("Opening stream from device.")
    result, stream = eb.PvStream.CreateAndOpen(connection_ID)
    if stream == None:
        logging.error(
            f"Unable to stream from device. {result.GetCodeString()} ({result.GetDescription()})")
    return stream


def configure_stream(device: eb.PvDevice, stream: eb.PvStream):
    """Configure the stream from the GigE Vision or USB3 Vision device

    Args:
        device (eb.PvDevice): The device object
        stream (eb.PvStream): The stream object
    """
    if isinstance(device, eb.PvDeviceGEV):
        # Negotiate packet size
        device.NegotiatePacketSize()
        # Configure device streaming destination
        device.SetStreamDestination(
            stream.GetLocalIPAddress(),  # type: ignore
            stream.GetLocalPort()  # type: ignore
        )


def configure_stream_buffers(device: eb.PvDevice, stream: eb.PvStream) -> list:
    """Configure the stream buffers from the GigE Vision or USB3 Vision device

    Args:
        device (eb.PvDevice): The device object
        stream (eb.PvStream): The stream object

    Returns:
        list: The list of buffers
    """
    buffer_list = []
    # Reading payload size from device
    size = device.GetPayloadSize()

    # Use BUFFER_COUNT or the maximum number of buffers, whichever is smaller
    buffer_count = stream.GetQueuedBufferMaximum()
    if buffer_count > BUFFER_COUNT:
        buffer_count = BUFFER_COUNT

    # Allocate buffers
    for _ in range(buffer_count):
        # Create new pvbuffer object
        pvbuffer = eb.PvBuffer()
        # Have the new pvbuffer object allocate payload memory
        pvbuffer.Alloc(size)
        # Add to external list - used to eventually release the buffers
        buffer_list.append(pvbuffer)

    # Queue all buffers in the stream
    for pvbuffer in buffer_list:
        stream.QueueBuffer(pvbuffer)
    logging.info(f"Created {buffer_count} buffers")
    return buffer_list


def acquire_images_for(device: eb.PvDevice, stream: eb.PvStream, record_for: int):
    """Acquire images from the GigE Vision or USB3 Vision device

    Args:
        device (eb.PvDevice): The device object
        stream (eb.PvStream): The stream object
        record_for (int): The amount of time to record for in seconds.
    """
    # Get device parameters need to control streaming
    device_params: eb.PvGenParameterArray = device.GetParameters()

    # Map the GenICam AcquisitionStart and AcquisitionStop commands
    start: eb.PvGenParameter = device_params.Get("AcquisitionStart")
    stop: eb.PvGenParameter = device_params.Get("AcquisitionStop")

    # Get stream parameters
    stream_params: eb.PvGenParameterArray = stream.GetParameters()

    # Map a few GenICam stream stats counters
    frame_rate: eb.PvGenParameter = stream_params.Get("AcquisitionRate")
    bandwidth: eb.PvGenParameter = stream_params["Bandwidth"]

    # Enable streaming and send the AcquisitionStart command
    logging.info("Enabling streaming and sending AcquisitionStart command.")

    device.StreamEnable()
    start.Execute()  # type: ignore

    time_when_started = time.perf_counter()

    while (time.perf_counter() - time_when_started < record_for):
        # Retrieve next pvbuffer
        result: eb.PvResult
        pvbuffer: eb.PvBuffer
        operational_result: eb.PvResult

        result, pvbuffer, operational_result = stream.RetrieveBuffer(1000)

        if result.IsOK():
            if operational_result.IsOK():
                # We now have a valid pvbuffer. This is where you would typically process the pvbuffer.
                _, frame_rate_val = frame_rate.GetValue()  # type: ignore
                _, bandwidth_val = bandwidth.GetValue()  # type: ignore

                logging.debug(f"BlockID: {pvbuffer.GetBlockID()}")

                payload_type: eb.PvPayloadType = pvbuffer.GetPayloadType()

                # Only process data if the payload type is image
                if payload_type == eb.PvPayloadTypeImage:
                    image: eb.PvImage = pvbuffer.GetImage()
                    image_data: np.ndarray = image.GetDataPointer()
                    logging.debug(
                        f" W: {image.GetWidth()} H: {image.GetHeight()}")

                    if opencv_is_available:

                        # This should never happen, but just in case
                        if image.GetPixelType() == eb.PvPixelRGB8:
                            image_data = cv2.cvtColor(
                                image_data, cv2.COLOR_RGB2BGR)

                        curr_timestamp_in_millis: int = int(
                            round(datetime.now().timestamp()*1000))
                        img_name = f"img_{curr_timestamp_in_millis}_fps_{frame_rate_val:.1f}_bw_{bandwidth_val / 1000000.0:.1f}.jpg"
                        imgs_dir = "imgs"

                        os.makedirs(imgs_dir, exist_ok=True)

                        time_when_starting_to_save_img = time.perf_counter()

                        # TODO: This code is blocking and causes the acquisition to only reach 3 FPS,
                        # we should make it async or implement a producer-consumer pattern
                        # see also:
                        #    https://github.com/alliedvision/VimbaPython/issues/62
                        cv2.imwrite(
                            os.path.join(imgs_dir, img_name),
                            image_data
                        )

                        time_when_img_saved = time.perf_counter()

                        logging.debug(
                            f"Time to save image: {time_when_img_saved - time_when_starting_to_save_img}")

                else:
                    logging.warn("Payload type not supported by this sample")
            else:
                # Non OK operational result
                logging.error(operational_result.GetCodeString())
            # Re-queue the pvbuffer in the stream object
            stream.QueueBuffer(pvbuffer)

        else:
            # Retrieve pvbuffer failure
            logging.error(result.GetCodeString())

    if opencv_is_available:
        cv2.destroyAllWindows()

    # Tell the device to stop sending images.
    logging.info("Sending AcquisitionStop command to the device")
    stop.Execute()  # type: ignore

    # Disable streaming on the device
    logging.info("Disable streaming on the controller.")
    device.StreamDisable()

    # Abort all buffers from the stream and dequeue
    logging.info("Aborting buffers still in stream")
    stream.AbortQueuedBuffers()
    while stream.GetQueuedBufferCount() > 0:
        result, pvbuffer, _ = stream.RetrieveBuffer()


def start_recording(record_for: int):
    """Starts recording video for a given amount of time.

    Args:
        record_for (int): The amount of time to record for in seconds.
    """
    logging.info("Starting recording")

    logging.info("PvStreamSample:")

    connection_ID: str = psu.PvSelectDevice()
    if connection_ID:
        device = connect_to_device(connection_ID)
        if device:
            stream = open_stream(connection_ID)
            if stream:
                configure_stream(device, stream)
                buffer_list = configure_stream_buffers(device, stream)
                acquire_images_for(device, stream, record_for)
                buffer_list.clear()

                # Close the stream
                logging.info("Closing stream")
                stream.Close()
                eb.PvStream.Free(stream)

            # Disconnect the device
            logging.info("Disconnecting device")
            device.Disconnect()
            eb.PvDevice.Free(device)
