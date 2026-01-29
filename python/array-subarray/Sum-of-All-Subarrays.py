class Solution:
    def subarraySum(self, A):
        ans = 0
        n = len(A)
        for i in range(n):
            ans += A[i] * (i + 1) * (n - i);
        return ans