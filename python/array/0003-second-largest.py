def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

def second_largest_1(arr):
    arr = list(set(arr))   # remove duplicates
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None

second_largest = lambda arr: sorted(set(arr))[-2]




