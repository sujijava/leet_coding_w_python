# if condition
# prevHeight > heights[r][c] or
# (r, c) in visit

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                prevHeight > heights[r][c] or
                (r, c) in visit
            ):
                return

            visit.add((r, c))
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS-1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS-1, c, atl, 0)

        return pac.intersection(atl)
