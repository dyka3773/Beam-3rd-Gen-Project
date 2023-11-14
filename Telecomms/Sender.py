import serial
from Frame import *

if __name__ == "__main__":
    # According to https://jetsonhacks.com/nvidia-jetson-nano-j41-header-pinout/
    # we will probably connect to the RXSM through the port `/dev/ttyTHS1` which requires
    # the GPIO pins 8 & 10
    serial_port = "/dev/ttyUSB0" #TODO which port is the port we connect to in rexus interface?
    baud_rate = 9600
    max_packet_size = 64
    try:
        port = serial.Serial(serial_port, baud_rate)
        print(f"Connected to {port.name}")

        for _ in range(10):
            frame = Frame("40AB851E")
            remaining_data = frame.getFrame()
            if frame.send_packet(max_packet_size):
                port.write(frame.getFrame())
                print(frame.getFrame())
            else: #split in packets
                while remaining_data:
                    frame.send_packet(remaining_data[:max_packet_size])  # Send up to max_packet_size characters
                    remaining_data = remaining_data[max_packet_size:] #TODO add exception

    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except KeyboardInterrupt:
        print("Serial communication terminated.")
    finally:
        # Close the serial port when done
        port.close()

#TODO error detection codes
#TODO fix frequency of sending data
#TODO implement sensor data decoder in our code