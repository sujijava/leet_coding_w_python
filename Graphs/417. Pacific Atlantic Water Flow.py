# if condition
# prevHeight > heights[r][c] or
# (r, c) in visit

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(heights)
        self.COLS = len(heights[0])        
        self.heights = heights
        
        pac = set()
        atl = set()

        for r in range(self.ROWS):
            self.dfs(r, 0, pac, 0)
            self.dfs(r, self.COLS-1, atl, 0)

        for c in range(self.COLS):
            self.dfs(0, c, pac, 0)
            self.dfs(self.ROWS-1, c, atl, 0)

        return pac.intersection(atl)
    
    def dfs(self, r, c, visit, prevHeight):
        if (
            r < 0 or
            c < 0 or
            r >= self.ROWS or
            c >= self.COLS or
            prevHeight > self.heights[r][c] or
            (r, c) in visit
        ):
            return

        visit.add((r, c))
        self.dfs(r, c+1, visit, self.heights[r][c])
        self.dfs(r, c-1, visit, self.heights[r][c])
        self.dfs(r+1, c, visit, self.heights[r][c])
        self.dfs(r-1, c, visit, self.heights[r][c])

'''
space complexity: O(MN)
time complexity: O(MN)
'''