class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) #make array in particular nums [2,3,4,5,10,20]
        longest = 0

        for n in nums: 
            if (n - 1) not in nums_set:
                count = 1
                while n + 1 in nums_set:
                    count +=1
                    n+=1
                longest = max(longest, count)
        return longest