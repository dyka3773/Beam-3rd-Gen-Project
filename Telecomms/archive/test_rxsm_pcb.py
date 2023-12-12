import serial

# Replace 'COM5' and 'COM6' with the virtual ports you created
# ser4 = serial.Serial('COM4', baudrate=9600, timeout=0.33)
ser4 = serial.Serial('/dev/ttyTHS1', baudrate=9600, timeout=0.33)

try:
    while True:
        # Send data
        data_to_send = "Hello, UART!"
        ser4.write(data_to_send.encode())

        print("Sent:", data_to_send)

        try:
            # Receive data
            data_received = ser4.readline()
            print("Received:", str(data_received, "utf-8"))
        except UnicodeDecodeError:
            print("Received:", data_received)

except KeyboardInterrupt:
    ser4.close()
