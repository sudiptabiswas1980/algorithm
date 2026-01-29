from collections import OrderedDict

def first_non_repeating(s):
    freq = OrderedDict()

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    for c, count in freq.items():
        if count == 1:
            return c

    return None
