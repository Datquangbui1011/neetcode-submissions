class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # create a set 
        for i in nums:  # loop through the array of input
            if i in seen: # if i in the set
                return True  # return True
            seen.add(i)  # Otherwise, add it into the set, keep going until the aray done
        return False  # return False if not duplicate