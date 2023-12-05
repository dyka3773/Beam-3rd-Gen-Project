import asyncio
from serial_asyncio import open_serial_connection


async def run():
    reader, writer = await open_serial_connection(url='COM6', baudrate=9600)
    while True:
        writer.write(b'Hello, UART!\n')

        await asyncio.sleep(1)

        line = await reader.readline()
        print(str(line, 'utf-8'))

if __name__ == '__main__':
    asyncio.run(run())
