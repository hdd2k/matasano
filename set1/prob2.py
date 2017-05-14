import util


def main():
  hexOne = '1c0111001f010100061a024b53535009181c'
  hexTwo = '686974207468652062756c6c277320657965'
  print( util.xor(util.hexToBin(hexOne), util.hexToBin(hexTwo)) )


if __name__ == "__main__":
  main()
