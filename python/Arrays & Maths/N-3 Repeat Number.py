class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        k = 3
        count = [0]*(k-1)
        cand = [-1]*(k-1)
        for i in range(n):
            j = 0
            # A[i] is checked if in cands
            while j < k-1:
                if cand[j] == A[i]:
                    count[j] += 1
                    break
                j += 1
            if j == k - 1:
                # A[i] is not in cands
                l = 0
                while l < k - 1:
                    if count[l] == 0:
                        cand[l] = A[i]
                        count[l] = 1
                        break
                    l += 1
                if l == k - 1:
                    # No candidate is empty. We need to ignore it and reduce counts by 1
                    for l in range(k-1):
                        count[l] -= 1
        
        # Check actual counts of candidates
        for i in range(k-1):
            temp = cand[i]
            tempCnt = 0
            for j in range(n):
                if A[j] == temp:
                    tempCnt += 1
            if tempCnt > n/k:
                return temp
        return -1