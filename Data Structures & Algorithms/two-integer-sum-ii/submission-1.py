class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l  = 0
        r = len(numbers) -1
        while (l <r):
            curr_num = numbers[l] + numbers[r]
            if curr_num == target:
                return [l+1, r+1]
            if curr_num <= target:
                l+=1
            else:
                r-=1
        return []