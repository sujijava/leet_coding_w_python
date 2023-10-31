from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        minute = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while len(rotten) > 0 and fresh > 0:
            size = len(rotten)
            for i in range(size):
                rotten_cell = rotten.popleft()
                r = rotten_cell[0]
                c = rotten_cell[1]

                # Check and rot neighboring fresh oranges with acceptable range conditions
                if r + 1 < ROWS and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    rotten.append((r + 1, c))
                    fresh -= 1

                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    rotten.append((r - 1, c))
                    fresh -= 1

                if c + 1 < COLS and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    rotten.append((r, c + 1))
                    fresh -= 1

                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    rotten.append((r, c - 1))
                    fresh -= 1

            minute += 1

        if fresh == 0:
            return minute
        else:
            return -1
