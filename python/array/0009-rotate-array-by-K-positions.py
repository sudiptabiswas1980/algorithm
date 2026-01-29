rotate = lambda arr, k: arr[-k % len(arr):] + arr[:-k % len(arr)]

