def rotate(arr, k):
    n = len(arr)
    k %= n  # handle k > n

    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
