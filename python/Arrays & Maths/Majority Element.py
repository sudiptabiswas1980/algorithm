class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority_idx = 0
        count = 1
        n = len(A)
        for i in range(1,n):
            if A[majority_idx] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_idx = i
                count = 1
        ret = A[majority_idx]
        count = 0
        for a in A:
            if a == ret:
                count += 1
        if count >= n/2:
            return ret
        return -1