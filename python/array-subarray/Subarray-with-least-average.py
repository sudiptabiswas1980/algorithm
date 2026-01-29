class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res=0
        summ=0
        for i in range(B) :
            summ+=A[i]
        n=len(A)
        min_sum=summ
        for i in range(B,n) :
            summ+=A[i]-A[i-B]
            if(summ<min_sum) :
                min_sum=summ
                res=i-B+1
        return res