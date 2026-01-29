import heapq
from collections import Counter

def kth_most_frequent(nums, k):
    freq = Counter(nums)

    # Max-heap using negative frequency
    # Order:
    # 1️⃣ Higher frequency first
    # 2️⃣ If tie → smaller number first
    heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(heap)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return heap[0][1]
