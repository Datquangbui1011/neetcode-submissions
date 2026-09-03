class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range (n):
            curr_sum =0

            for j in range (i, n):
                curr_sum = curr_sum + nums[j]
                res = max(res, curr_sum)
        return res