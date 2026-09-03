class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create the unique set
        for num in nums: # read all elements in the List
            if num in seen: # if number is seen before (similar number)
                return True  # return true
            seen.add(num)     # else add that element to set()
        return False         # return false


        