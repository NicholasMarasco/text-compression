import sys
from arithmetic import *

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
            with open("e_output2.bnr","ab") as f:
                f.write(self.buffer.to_bytes(1, 'little'))
            self.bits_to_go = 8

    def flush_buffer(self):
#         with open("e_output.txt","a") as f:
#             f.write(chr(self.buffer>>self.bits_to_go))
        with open("e_output.bnr","ab") as f:
            f.write(self.buffer.to_bytes(1, 'little'))

class BitInputStream:

    def __init__(self):
        self.buffer = 0
        self.bits_to_go = 0
        self.garbage_bits = 0
        self.f = open("e_output2.bnr","rb")

    def input_bit(self):
        if(self.bits_to_go == 0):
            self.buffer = int.from_bytes(self.f.read(1),'little')
            if not self.buffer:
                self.garbage_bits += 1
                if(self.garbage_bits > Code_value_bits-2):
                    print("Bad input file")
                    sys.exit(1)
            self.bits_to_go = 8
        t = self.buffer & 1
        self.buffer = self.buffer >> 1
        self.bits_to_go -= 1
        return t

    def close(self):
        self.f.close()
