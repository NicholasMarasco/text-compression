#include "model.h"

int freq[No_of_symbols+1];

start_model()
{
  int i;
  for(i = 0; i < No_of_chars; i++){
    char_to_index[i] = i+1;
    index_to_char[i+1] = i;
  }
  for(i = 0; i <= No_of_symbols; i++){
    freq[i] = 1;
    total_freq[i] = No_of_symbols-i;
  }
  freq[0] = 0;
}

update_model(symbol)
  int symbol;
{
  int i;
  if(total_freq[0] == Max_freq){
    int total;
    total = 0;
    for(i = No_of_symbols; i >= 0; i--){
      freq[i] = (freq[i]+1)/2;
      total_freq[i] = total;
      total += freq[i];
    }
  }
  for(i = symbol; freq[i] == freq[i-1]; i--);
  if(i < symbol){
    int ch_i, ch_symbol;
    ch_i = index_to_char[i];
    ch_symbol = index_to_char[symbol];
    index_to_char[i] = ch_symbol;
    index_to_char[symbol] = ch_i;
    char_to_index[ch_i] = symbol;
    char_to_index[ch_symbol] = i;
  }
  freq[i] += 1;
  while(i > 0){
    i--;
    total_freq[i]++;
  }
}
