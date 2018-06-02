from decoders import Decoder
from model import Model

def main():
    model = Model()
    decoder = Decoder()
    with open("d_output.txt","w") as f:
        while(True):
            symbol = decoder.decode_symbol(model.total_freq)
            print(symbol)
            if(symbol == model.EOF_SYMBOL):
                break
            ch = model.index_to_char[symbol]
            f.write(chr(ch))
            model.update_model(symbol)
        decoder.close()

if __name__ == "__main__":
    main()
