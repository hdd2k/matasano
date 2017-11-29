
# TODO: Refactor to use method dispatching (http://python-3-patterns-idioms-test.readthedocs.io/en/latest/MultipleDispatching.html)

# Use [binascii] module to convert bin <---> ASCII encoded binary representations
# Working with Binary data in Python
# ----- (https://www.devdungeon.com/content/working-binary-data-python)
# ----- (http://www.bogotobogo.com/python/python_bits_bytes_bitstring_constBitStream.php)


############################
# Note : Always operate on raw bytes!!! Not encoded strings
############################

import binascii
import codecs



############################
# Convert String rep ---> Raw binary data (bytes)
############################
def hex_2_raw(hex_str):
    return binascii.unhexlify(hex_str)

def bin_2_raw(bin_str):
    pass
    # return int(bin_str, 2)

def base64_2_raw(base64_str):
    pass


############################
# Convert Raw binary data (bytes) ---> String rep
############################
def raw_2_hex(raw_hex):
    return binascii.hexlify(raw_hex)

def raw_2_bin(raw_bin):
    pass

def raw_2_base64(raw_base64):
    # Note : returns correct string, BUT in binary bytes type ---> decode as (utf-8)
    return binascii.b2a_base64(raw_base64).decode('utf-8').strip()



############################
# Raw binary data operations
############################

def xor(raw1, raw2):
    return bytes(c1^c2 for c1,c2 in zip(raw1, raw2))






