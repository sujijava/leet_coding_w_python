import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 
        pivot = random.choice(nums)
        left = [ x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if L >= k:
            return self.findKthLargest(left, k)
        elif L + M <k:
            return self.findKthLargest(right, k-L-M)
        else:
            return mid[0]

