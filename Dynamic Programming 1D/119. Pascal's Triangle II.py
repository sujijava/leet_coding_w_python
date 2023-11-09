import pdb
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        row = [1,1]
        for i in range(1,rowIndex):
            prevRow = row
            pdb.set_trace()  # This line sets a breakpoint
            row.insert(i, prevRow[i-1]+prevRow[i])
            print(prevRow)
        return row 

s = Solution()
s.getRow(3)
