# Input: matrix = [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ], target = 3
# Output: true

# Summary: BST search

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid_index = (l + r) // 2
            mid = matrix[mid_index // n][mid_index % n]
            if mid < target:
                l = mid_index + 1
            elif mid > target:
                r = mid_index - 1
            elif mid == target:
                return True

        return False
