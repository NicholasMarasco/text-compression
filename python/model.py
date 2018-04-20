class Model:

    def __init__(self):
        self.NUM_CHARS   = 256
        self.EOF_SYMBOL  = (self.NUM_CHARS+1)
        self.NUM_SYMBOLS = (self.NUM_CHARS+1)
        self.MAX_FREQ    = 16383

        self.char_to_index = [None] * self.NUM_CHARS
        self.index_to_char = [None] * (self.NUM_SYMBOLS + 1)
        self.total_freq    = [None] * (self.NUM_SYMBOLS + 1)
        self.freq          = [None] * (self.NUM_SYMBOLS + 1)

        for i in range(0,self.NUM_CHARS):
            self.char_to_index[i] = i+1
            self.index_to_char[i+1] = i
        for i in range(0,self.NUM_SYMBOLS+1):
            self.freq[i] = 1
            self.total_freq[i] = self.NUM_SYMBOLS-i
        self.freq[0] = 0

    def update_model(self, symbol):
        if (self.total_freq[0] == self.MAX_FREQ):
            total = 0
            for i in range(self.NUM_SYMBOLS,-1,-1):
                self.freq[i] = (self.freq[i]+1)/2
                self.total_freq[i] = total
                total += self.freq[i]
        i = symbol
        while self.freq[i] == self.freq[i-1]:
            i -= 1
        if (i < symbol):
            ch_i      = self.index_to_char[i]
            ch_symbol = self.index_to_char[symbol]
            self.index_to_char[i] = ch_symbol
            self.index_to_char[symbol] = ch_i
            self.char_to_index[ch_i] = symbol
            self.char_to_index[ch_symbol] = i
        self.freq[i] += 1
        while i > 0:
            i -= 1
            self.total_freq[i] += 1
