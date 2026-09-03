class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)  # initialize the n array first
        ans = [None] * (2 *n)  # create a list with 2n of nums list
        for i in range (n):   # loop throug the nums list
            ans[i] = nums[i]   # First line: copy nums[i] to the first half of ans.
            ans[i + n] = nums[i] # Second line: copy nums[i] to the second half of ans.
        return ans #Return the fully concatenated array.