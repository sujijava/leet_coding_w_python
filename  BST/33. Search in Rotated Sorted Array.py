from typing import List

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# logic 
# 1. finding the ascending potion of array 
# 2. if target is in ascending portion, search inside of ascending portion
# 3. otherwise, search outside of ascending portion

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        mid = (l + r) // 2
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
        
            if nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1 
                else: 
                    r = mid - 1
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else: 
                    l = mid + 1
        
        return -1