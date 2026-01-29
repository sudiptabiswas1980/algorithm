public class Solution {
    public int maxSubArray(final List<Integer> A) {
        int curSum = 0; //is the maximum sum ending at any given index i
        int maxSum = Integer.MIN_VALUE; // maximum subarray sum for all subarrays till now
	    for (int num : A) {
	        curSum += num;
            maxSum = Math.max(maxSum, curSum);
            if (curSum < 0) curSum = 0;
	    }
	    return maxSum;
    }
}