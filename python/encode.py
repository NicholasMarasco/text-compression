from encoders import Encoder
from model import Model

def main():
    global model,encoder
    model = Model()
    encoder = Encoder()
    with open("25_alpha.txt") as f:
        for line in f:
            if doLine(line):
                break
    encoder.encode_symbol(model.EOF_SYMBOL, model.total_freq)
    encoder.done_encoding()

def doLine(line):
    for c in line:
        if not c:
            return 1
        symbol = model.char_to_index[ord(c)]
        encoder.encode_symbol(symbol, model.total_freq)
        model.update_model(symbol)

if __name__ == "__main__":
    main()
