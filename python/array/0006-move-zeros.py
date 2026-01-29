def move_zeros(arr):
    index = 0  # position to place next non-zero

    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1

    # fill remaining positions with zeros
    for i in range(index, len(arr)):
        arr[i] = 0
