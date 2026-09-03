class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # for i in range (n):
        #     if nums[i] == target:
        #         return i
        # return -1
        # this is the brute force O(n)

        # Binary search O(log n)
        # L,H = 0 , n -1
        # while l < h:
        # find mid 
        # if mid == target:
        # return mid
        # We split into have before and after mid
        # if nums[low]< nums[mid]:
        #    if nums[low] < target <= nums[mid]:
        #       high = mid - 1
        #    else:
        #        low = mid -1 

        # else:
        #     if nums[mid] < target <= nums[high]
        #       low = mid +1
        #      else:
        #       high = mid -1
        #return -1



        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1 

            else:
                if nums[mid] < target <= nums[high]:
                    low = mid +1
                else:
                    high = mid -1
        return -1

