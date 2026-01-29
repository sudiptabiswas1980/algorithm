class Solution:
    def solve(self, A, B):
        n = len(A)
        pref = [0] * (n)
        pref[0] = A[0]
        for i in range(1, n):
            pref[i]=pref[i-1]+A[i]
        ans = 0
        for i in range(n):
            for j in range(i,n):
                val = pref[j]
                if(i>0):
                    val -= pref[i-1]
                if val<B: ans+=1
        return ans