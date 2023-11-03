# Input: nums = [2,3,-2,4]
# Output: 6

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = 1 
        curMax = 1 
        maxProduct = nums[0]
        
        for n in nums: 
            temp = n * curMax 
            curMax = max(n, temp, n*curMin) 
            curMin = min(n, temp, n*curMin)
            maxProduct = max(maxProduct, curMax) 
            
        return maxProduct
