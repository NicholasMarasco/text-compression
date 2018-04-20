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
#             with open("e_output.txt","a") as f:
#                 f.write(chr(self.buffer))
            with open("e_output.bnr","ab") as f:
                f.write(self.buffer.to_bytes(1, 'little'))
            self.bits_to_go = 8

    def flush_buffer(self):
#         with open("e_output.txt","a") as f:
#             f.write(chr(self.buffer>>self.bits_to_go))
        with open("e_output.bnr","ab") as f:
            f.write(self.buffer.to_bytes(1, 'little'))
