class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        l1 = []
        n = len(A)
        length = 2 * B + 1
        for i in range(n - length + 1):
            curr = -1
            flag = 1
            for j in range(i, i + length):
                if (A[j] == curr):
                    flag = 0
                    break
                curr = A[j]
            if (flag == 1):
                l1.append(i + B)
        return l1