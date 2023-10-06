class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.COLS = len(board[0])
        self.ROWS = len(board)
        visit = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if r == 0 or r == self.ROWS - 1 or c == 0 or c == self.COLS - 1:
                    self.unsurrounded_cell_marker(board, r, c, visit)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

    def unsurrounded_cell_marker(self, board, r, c, visit):
        if r < 0 or c < 0 or c >= self.COLS or r >= self.ROWS or board[r][c] != "O" or (r, c) in visit:
            return
        board[r][c] = "T"
        visit.add((r, c))
        self.unsurrounded_cell_marker(board, r+1, c, visit)
        self.unsurrounded_cell_marker(board, r, c+1, visit)
        self.unsurrounded_cell_marker(board, r-1, c, visit)
        self.unsurrounded_cell_marker(board, r, c-1, visit)
