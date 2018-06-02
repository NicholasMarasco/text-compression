from arithmetic import *
from bit_io import BitInputStream

class Decoder:

    def __init__(self):
        self.input = BitInputStream()
        self.value = 0
        for i in range(1,Code_value_bits+1):
            self.value = 2* self.value + self.input.input_bit()
        self.low = 0
        self.high = Top_value

    def decode_symbol(self, total_freq):
        dRange = (self.high - self.low)+1
        total = (((self.value - self.low) + 1) * total_freq[0] - 1) / dRange
        symbol = 1
        while(total_freq[symbol] > total):
            symbol += 1
        self.high = self.low + (dRange * total_freq[symbol-1])/total_freq[0]-1
        self.low = self.low + (dRange * total_freq[symbol])/total_freq[0]
        while(True):
            if(self.high < Half):
                pass
            elif(self.low >= Half):
                self.value -= Half
                self.low -= Half
                self.high -= Half
            elif(self.low >= First_qtr and self.high < Third_qtr):
                self.value -= First_qtr
                self.low -= First_qtr
                self.high -= First_qtr
            else:
                break
            self.low = 2 * self.low
            self.high = 2 * self.high + 1
            self.value = 2 * self.value + self.input.input_bit()
        return symbol

    def close(self):
        self.input.close()
