import serial

# Replace 'COM5' and 'COM6' with the virtual ports you created
ser5 = serial.Serial('COM5', baudrate=9600, timeout=0.33)
ser6 = serial.Serial('COM6', baudrate=9600, timeout=0.33)

try:
    while True:
        # Send data
        data_to_send = "Hello, UART!"
        ser5.write(data_to_send.encode())

        # Read data
        received_data = ser6.readline().decode().strip()
        print("Received:", received_data)

except KeyboardInterrupt:
    ser5.close()
    ser6.close()
