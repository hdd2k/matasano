import util

def main():
  # 'hexStr' : has been XOR-ed against 1 character
  hexStr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
  util.freq_analysis(hexStr)
# TODO: use frequency analysis ('e' is most frequent, etc, etc)


if __name__ == "__main__":
  main()
