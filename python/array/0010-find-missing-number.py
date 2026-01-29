class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        nums.sort()
        out = n

        for i in range(n):
            if i != nums[i]:
                out = i
                break

        return out
