import serial
from Frame import *

if __name__ == "__main__":
    serial_port = '/dev/ttyS0'
    baud_rate = 9600
    try:
        # Open the serial port
        ser = serial.Serial(serial_port, baudrate=baud_rate, timeout=1)

        # Continuously read data from the RS-422 port
        while True:
            data = ser.readline()
            received_data = ser.readline().decode('utf-8').strip()
            if received_data:
                print(f"Received: {received_data}")

            if len(data) >= 1:
                # frame = Frame(data)
                # frame.printf()
                # print(frame.isValid())
                print(data.hex() + "\n")
    except serial.SerialException as e:
        print(f"Serial port error: {e}")
    except KeyboardInterrupt:
        print("Serial communication terminated.")
    finally:
        # Close the serial port when done
        ser.close()


#TODO verify checksum integrity (crc)


