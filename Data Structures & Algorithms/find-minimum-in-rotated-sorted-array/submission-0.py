class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input: array in ascending order, 
        # output: find the minimum of rotate
        # [1,2,3,4,5,6] = > [2,3,4,5,6,1] => [3,4,5,6, 1,2,] => [3,4,5,6,1,2] 
        # 2 time rotate => min(2 time) = 1


        # l = 0, r = n -1
        # [3,4,5,6,1,2] 
        #          mr
        #           l 



        return min(nums)
        