class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.currArea = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j) 
                    self.maxArea = max(self.currArea, self.maxArea)
                    self.currArea = 0

        return self.maxArea

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) -1 or j >len(grid[0]) -1 or grid[i][j] != 1:
            return 
        grid[i][j] = 8
        self.currArea = self.currArea + 1 
        self.dfs(grid, i+1, j) 
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)

'''
Time Complexity: 
O(R∗C)
Space complexity: 
O(R∗C)
'''