#include <stdio.h>
#include "model.h"

main(int ARGC, char *ARGV[])
{
  start_model();
  start_outputing_bits();
  start_encoding();
  for(;;){
    int ch, symbol;
    FILE *file;
    file = fopen(ARGV[1], "r")
    ch = fgetc(file);
    if(ch == EOF) break;
    symbol = char_to_index[ch];
    encode_symbol(EOF_symbol,total_freq);
    update_model(symbol);
  }
  encode_symbol(EOF_symbol,total_freq);
  done_encoding();
  done_outputing_bits();
  exit(0);
}
