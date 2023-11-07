from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum (nums) % 2:
            return False
        prevLevelDP = set()
        prevLevelDP.add(0)
        target = sum (nums) // 2
        for i in range (len (nums)- 1, -1, -1):
            currLevelDP = set()
            for t in prevLevelDP:
                if (t + nums[i]) == target:
                    return True
                # every number has two choices:
                # include itself or not
                currLevelDP.add(t+nums[i])
                currLevelDP.add(t)

            prevLevelDP = currLevelDP

s = Solution()
s.canPartition([1,5,11,5])
