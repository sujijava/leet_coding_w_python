class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0 
        res = nums[0]

        for n in nums:
            total += n 
            res = max(total, res)
            if total < 0:
                total = 0 
        return res
        