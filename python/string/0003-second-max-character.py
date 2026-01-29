from collections import Counter

def secmax(inp):
    counts = Counter(inp)
    freq_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    if len(freq_list) < 2:
        return (None, None)

    max_freq = freq_list[0][1]

    # Find second max frequency
    secondmax = None
    for _, freq in freq_list[1:]:
        if freq < max_freq:
            secondmax = freq
            break

    if secondmax is None:
        return (None, None)

    # Collect elements with second max frequency
    arr = [elem for elem, freq in freq_list if freq == secondmax]

    return (arr, secondmax)
