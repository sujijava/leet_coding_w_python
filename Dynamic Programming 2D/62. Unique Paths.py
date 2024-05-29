class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    grid[r][c] = 1 
                else: 
                    grid[r][c] = grid[r-1][c] + grid[r][c-1]

        return grid[m-1][n-1] 