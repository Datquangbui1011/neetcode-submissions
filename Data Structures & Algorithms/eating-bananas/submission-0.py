class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l =1 
        r = max(piles)

        while l < r:
            k = (l + r) //2
            hours = sum((p + k - 1) // k for p in piles)

            if hours <= h:
                r = k
            else:
                l = k + 1

        return l