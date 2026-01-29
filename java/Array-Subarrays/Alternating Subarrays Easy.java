class Solution {
    public int[] solve(int[] A, int B) {
        ArrayList < Integer > l1 = new ArrayList < > ();
        int n = A.length;
        int len = 2 * B + 1;
        for (int i = 0; i < n - len + 1; i++) {
            int curr = -1;
            int flag = 1;
            for (int j = i; j < i + len; j++) {
                if (A[j] == curr) {
                    flag = 0;
                    break;
                }
                curr = A[j];
            }
            if (flag == 1) {
                l1.add(i + B);
            }
        }
        int[] ret = new int[l1.size()];
        for (int i = 0; i < l1.size(); i++) {
            ret[i] = l1.get(i);
        }
        return ret;
    }
}