from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == c == 0:
                    continue 
                    
                left_path = up_path = float('inf')
                if r != 0:
                    up_path = grid[r][c] + grid[r-1][c]
                if c != 0:
                    left_path = grid[r][c] + grid[r][c-1]
                
                    
                grid[r][c] = min(left_path, up_path)
        return grid[ROWS-1][COLS-1]

s = Solution()
grid = [[1,2,3],[4,5,6]]
print(s.minPathSum(grid))


