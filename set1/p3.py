
# Note :
# ---- http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/ (for writeup)
# ---- https://stackoverflow.com/questions/6690739/fuzzy-string-comparison-in-python-confused-with-which-library-to-use

in_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

freq_seq = "ETAO"#INSHRDLU"
# freq_seq = "ETAOINSHRDLU"

from util import xor, raw_2_base64, hex_2_raw

def freq_dict(str):
    from collections import defaultdict
    d = defaultdict(int)
    for c in str:
        d[c] += 1
    return dict(d)

# Finding string similarity with percentage
# https://stackoverflow.com/questions/17388213/find-the-similarity-percent-between-two-strings
from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def freq_distance(lst):
    candidate_str = ''.join([x[0] for x in lst])
    print("####### candidate_str : {}".format(candidate_str))
    return similar(freq_seq.lower(), candidate_str.lower())


#
# Main Logic
#

print('input : [{}]'.format(in_str))

max_score = -1
max_entry = None

for i in range(pow(2,8)):
    # For each char
    c = i.to_bytes(1, 'big')
    # Pad to input string length
    padded = c * int(len(in_str) * (4 / 8))
    print("##### char : {} ##### padded : {}".format(padded))

    continue


    # XOR to get result
    result = raw_2_base64(
        xor(
            padded,
            hex_2_raw(in_str)
        )
    )
    # print result
    print("result : {}".format(result))
    # Create Frequency ordered dict
    freq = freq_dict(result)

    ordered_entries_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(ordered_entries_list)

    # Compare result with normal frequency
    score = freq_distance(ordered_entries_list[:4])
    print(score)

    if (score > max_score):
        max_score = score
        max_entry = result

    # break

print(max_score)
print(max_entry)








