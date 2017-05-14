# Utility classes and helper functions for this set

base64_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Enum types for string types --- indexed by (0,1,2)
class StringTypes:
  binary, hexa, base64 = range(3)


##### Use Binary string representation as common conversion representation

def hexToBin(hex_str):
  # {0:f} := 0^th position arg to 'format' function!!! and 'f' is the desired format
  # TODO: Replacement fields REQUIRE curly brackets!!!!! {}{}{} to substitute args!!!
  # TODO: no spaces!!!!! in the format string
  return ''.join( ['{0:04b}'.format( int(c, 16) ) for c in hex_str] )

# TODO: Handle edge case where bin_str length % 4 != 0
def binToHex(bin_str):
  return ''.join( [ '{0:x}'.format( int( binchunk, 2 ) ) for binchunk in [ bin_str[i : i + 4] for i in range(0,len(bin_str),4) ] ])

def base64ToBin(base64_str):
  # {0:f} := 0^th position arg to 'format' function!!! and 'f' is the desired format
  return ''.join( ['{0:06b}'.format( base64_map.find(c) ) for c in base64_str] )

def binToBase64(bin_str):
  return ''.join( [ base64_map[ int( binchunk, 2 ) ]  for binchunk in [ bin_str[i : i + 6] for i in range(0,len(bin_str),6) ] ] )

def hexToBase64(hex_str):
  return binToBase64( hexToBin(hex_str) )

def base64Tohex(base_str):
  return binToHex( base64ToBin(base_str) )

def xor(binStrOne, binStrTwo):
  # assume same length
  return binToHex(''.join( ['0' if ( binStrOne[i] == binStrTwo[i] ) else '1' for i in range(len(binStrOne))] ))

def freq_analysis(hexStr):
# XOR with ALL possible hex chars (16)
  # print(hexStr)
  # base64_map
  # for key in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']:
  for key in base64_map:
    print(key)
    encoded = xor(hexToBin(hexStr), base64ToBin( ''.join( len(hexStr) * [key] ) ))
    # TODO: list ---> frequency dictionary (using defaultdict)
    # create dictionary with num entries
    from collections import defaultdict
    freq_dict = defaultdict(int)
    for c in encoded:
      freq_dict[c] += 1
    # print(encoded)
    # print(freq_dict)
    # TODO: from dict, get items & sort by key=operator.itemgetter(1)
    # Order by num entries
    import operator
    freq_entries = sorted( freq_dict.items() , key=operator.itemgetter(1), reverse = True)
    # print( freq_entries[0] )
    # print( freq_entries)
    if (freq_entries[0][0] == 'e'):
      print(freq_entries[0])
    print(encoded)
    print("####################")

  # [Create score by sum(difference in expected & actual rank) for each char] match ordering with most frequent (keep track of least deviating iteration)

  most_freq = 'etaoinshrdlu'


