import eBUS as eb
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s',
    filename='rocket.log',
    encoding='utf-8',
    filemode='a'
)


def PvSelectDevice() -> str:
    """ Selects a device on the network.

    Returns:
        str: The connection ID of the selected device.
    """
    lSystem = eb.PvSystem()

    logging.info("Detecting devices.")

    lSystem.Find()

    # Detect, select device.
    lDIVector: list[eb.PvDeviceInfo] = []

    for i in range(lSystem.GetInterfaceCount()):
        lInterface: eb.PvInterface = lSystem.GetInterface(i)

        logging.info(f"[AVAILABLE DEVICE] {lInterface.GetDisplayID()}")

        if lInterface.GetDeviceCount() == 0:
            logging.warn(
                f"No device found for interface {lInterface.GetDisplayID()}")
            continue

        for j in range(lInterface.GetDeviceCount()):
            lDI: eb.PvDeviceInfo = lInterface.GetDeviceInfo(j)
            lDIVector.append(lDI)
            logging.info(f"[{len(lDIVector) - 1}]\t{lDI.GetDisplayID()}")

    if len(lDIVector) == 0:
        logging.error(f"No device found!")
        return ""

    lSelectedDI = lDIVector[0]

    # Is the IP Address valid?
    if lSelectedDI.IsConfigurationValid():
        return lSelectedDI.GetConnectionID()
    else:
        return ""
