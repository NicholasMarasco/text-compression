class BitOutStream:

    def __init__(self):
        self.buffer = 0
        self.bits_to_go = 8

    def output_bit(self, bit):
        self.buffer >>= 1
        if(bit):
            self.buffer |= 0x80
        self.bits_to_go -= 1
        if(self.bits_to_go == 0):
#             print(chr(self.buffer))
            self.bits_to_go = 8

    def flush_buffer(self):
        print(chr(self.buffer>>self.bits_to_go))
