# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Summary 
# BST
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#  l                 m             h
#  l        m     h
#             l/m h
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        while lo <= hi:
            mid_index = (lo + hi) // 2  
            curr_total_time = 0
            for p in piles:
                time_per_pile = math.ceil(float(p) / mid_index)
                curr_total_time += time_per_pile
            if curr_total_time <= h:
                res = mid_index
                hi = mid_index - 1
            else:
                lo = mid_index + 1
        return res

s = Solution()
s.minEatingSpeed([3,6,7,11], 8)