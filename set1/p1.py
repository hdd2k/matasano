in_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
out_str = "SSdtIGtpbGxpbmcgeW92ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

from util import hex_2_raw, raw_2_base64

print('input : [{}]'.format(in_str))
print('expected output : [{}]'.format(out_str))
print('real output     : [{}]'.format(raw_2_base64(hex_2_raw(in_str))))
