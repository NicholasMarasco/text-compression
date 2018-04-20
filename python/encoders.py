from arithmetic import *
from bit_io import *

class Encoder:

    def __init__(self):
        self.low = 0
        self.high = Top_value
        self.bits_to_follow = 0
        self.out = BitOutStream()

    def bit_plus_follow(self, bit):
        self.out.output_bit(bit)
        while(self.bits_to_follow > 0):
            self.out.output_bit(not bit)
            self.bits_to_follow -= 1

    def encode_symbol(self, symbol, total_freq):
        eRange = (self.high - self.low) + 1
        self.high = self.low + (eRange*total_freq[symbol-1])/total_freq[0] - 1
        self.low  = self.low + (eRange*total_freq[symbol])/total_freq[0]
        while(True):
            if(self.high < Half):
                self.bit_plus_follow(0)
            elif(self.low >= Half):
                self.bit_plus_follow(1)
                self.low -= Half
                self.high -= Half
            elif(self.low >= First_qtr and self.high < Third_qtr):
                self.bits_to_follow += 1
                self.low -= First_qtr
                self.high -= First_qtr
            else:
                break
            self.low  = 2*self.low
            self.high = 2*self.high+1

    def done_encoding(self):
        self.bits_to_follow += 1
        if(self.low < First_qtr):
            self.bit_plus_follow(0)
        else:
            self.bit_plus_follow(1)
        self.out.flush_buffer()
