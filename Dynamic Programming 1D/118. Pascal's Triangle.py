from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:       
        pascal = [[1]*(i+1) for i in range(numRows)]
        # pascal = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
        for r in range(numRows):
            for c in range(1,r):
                # combinations 
                # - (r,c) (2,1) (3,1) (3,2) (4,1) (4,2) (4,3)
                pascal[r][c] = pascal[r-1][c-1] + pascal[r-1][c]
        return pascal

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

s = Solution()
s.generate(5)