import heapq

def second_largest(arr):
    return heapq.nlargest(2, set(arr))[-1]
