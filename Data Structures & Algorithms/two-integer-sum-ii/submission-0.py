class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while(l < r):
            cur_num = numbers[r]+ numbers[l]
            if cur_num == target:
                return [l+1, r +1]
            if(cur_num < target):
                l+=1
            else:
                r-=1
        return []
            
        