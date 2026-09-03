class Solution:
    def searchMatrix(self, matrix: List[List[int]], x: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        lo, hi = 0 , n*m -1

        while lo <= hi:
            mid = (lo + hi) // 2

            row = mid // m
            col = mid % m

            if matrix[row][col] == x:
                return True

            if matrix[row][col] < x:
                lo = mid + 1
            else:
                hi = mid -1

        return False