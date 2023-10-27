# Input: m = 3, n = 7
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):  # 0,1
            newRow = [1] * n  # [1,1,1,1,1,1,1]
            for j in range(n-2, -1, -1):  # 5,4,3,2,1,0
                newRow[j] = newRow[j+1] + row[j]
            row = newRow

        return row[0]
