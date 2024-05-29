class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        routes = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.path = "" # <<<< ********* IMPTT ************
                if grid[r][c] == 1:
                    self.dfs(grid, r, c, 'o')
                    routes.add(self.path)
                
        return len(routes)

    def dfs(self, grid, r, c, direction):
        if r < 0 or c < 0:
            return 
        if r >= self.ROWS or c >= self.COLS:
            return 
        if grid[r][c] != 1:
            return 
        
        grid[r][c] = 8 # visited 
        self.path += direction

        self.dfs(grid, r+1, c, 'u')
        self.dfs(grid, r-1, c, 'd')
        self.dfs(grid, r, c+1, 'r')
        self.dfs(grid, r, c-1, 'l')
        
        self.path += 'b' # <<<< ********* IMPTT ************