# nums = [2,3,0,1,4]

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        start, end = 0, 0 
        
        while end < len(nums) -1:
            maxJump = 0 # 1,2 
            for i in range(start, end +1):
                maxJump = max(nums[i]+i, maxJump)
            start = end + 1 # 1
            end = maxJump # 2 
            res += 1

        return res 