def crc(data: bytes):
    crc = 0xffff
    for cur_byte in data:
        crc = crc ^ cur_byte
        for _ in range(8):
            a = crc
            carry_flag = a & 0x0001
            crc = crc >> 1
            if carry_flag == 1:
                crc = crc ^ 0xa001
    return bytes([crc % 256, crc >> 8 % 256])


class Frame:
    countFrames = 0

    def __init__(self, data):
        if isinstance(data, str):
            self.start1 = bytes.fromhex("50")
            self.start2 = bytes.fromhex("AF")
            self.countFrames += 1
            self.segID = self.countFrames.to_bytes(1, "big")
            self.payload = bytes.fromhex(data)
            self.end1 = bytes.fromhex("50")
            self.end2 = bytes.fromhex("A5")
            self.frame = self.__buildFrame()
            self.crc = crc(self.frame)
            self.frame += self.crc
        else:
            self.payload = bytes()
            self.start1 = data[0].to_bytes(1, "big")
            self.start2 = data[1].to_bytes(1, "big")
            self.segID = data[2].to_bytes(1, "big")
            for i in range(3, 7):
                self.payload += data[i].to_bytes(1, "big")
            self.end1 = data[7].to_bytes(1, "big")
            self.end2 = data[8].to_bytes(1, "big")
            self.crc = data[9].to_bytes(1, "big") + data[10].to_bytes(1, "big")
            self.frame = data

    def __buildFrame(self) -> bytes:
        return self.start1 + self.start2 + self.segID + self.payload + self.end1 + self.end2

    def getFrame(self) -> bytes:
        return self.frame

    def isValid(self) -> bool:
        return crc(self.frame) == (0).to_bytes(2, "big")

    def printf(self):
        print(self.start1.hex() + ", " + self.start2.hex() + ", " + self.segID.hex() + ", " + self.payload.hex() + ", " + self.end1.hex() + ", " + self.end2.hex() + ", " + self.crc.hex())

    def send_packet(self,max_packet_size):
        # Ensure data length does not exceed the maximum packet size
        if len(self.frame) <= max_packet_size:
            return True
        else:
            print("Data exceeds maximum packet size.")
            return False