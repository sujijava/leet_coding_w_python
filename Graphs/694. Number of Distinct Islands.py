class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.steps = ''
        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 'o' for origin
                    self.helper(grid, i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        print(distinctIslands)
        return len(distinctIslands)
    
    def helper(self, grid, i, j, direct):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            self.steps += direct
            grid[i][j] = 8 # mark as visited
            self.helper(grid, i+1, j, 'd')  # down
            self.helper(grid, i-1, j, 'u')  # upper
            self.helper(grid, i, j+1, 'r')  # right
            self.helper(grid, i, j-1, 'l')  # left
            self.steps += 'b'  # back
s = Solution()
# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
s.numDistinctIslands(grid)