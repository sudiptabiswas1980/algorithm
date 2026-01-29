public class Solution {
    public int solve(int[] A, int B) {
        int n  = A.length;
        int pref[] = new int[n];
        pref[0]=A[0];
        int ans=0;
        for(int i=1;i<n;i++)pref[i]=pref[i-1]+A[i];
        for(int i=0;i<n;i++){
            for (int j=i;j<n;j++){
                int sum = pref[j];
                if(i>0){
                    sum -= pref[i-1];
                }
                if(sum < B) ans++;
            }
        }
        return ans;
    }
}