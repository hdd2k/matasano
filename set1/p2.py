in_1_str = "1c0111001f010100061a024b53535009181c"
in_2_str = "686974207468652062756c6c277320657965"
out_str = "746865206b696420646f6e277420706c6179"

from util import xor, raw_2_hex, hex_2_raw

print('input 1 : [{}]'.format(in_1_str))
print('input 2 : [{}]'.format(in_2_str))
print('expected output : [{}]'.format(out_str))
print('real output     : [{}]'.format(
    raw_2_hex(
        xor(
            hex_2_raw(in_1_str),
            hex_2_raw(in_2_str)
        )
    ).decode('utf-8')
))

