# You are given an integer array nums and an integer k.

# In one operation, 
# you can pick two numbers from the array whose sum equals k 
# and remove them from the array.

# Return the maximum number of operations 
# you can perform on the array.

# Input: nums = [1,2,3,4], k = 5
# Output: 2

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted = nums.sort()
        l = 0
        r = len(sorted) - 1
        ans = 0

        while l < r:
            l_num = nums[l]
            r_num = nums[r]
            if l_num + r_num == k:
                ans = ans + 1
                del nums[l]
                del nums[r]
            elif l_num + r_num > k:
                r = r - 1
            elif l_num + r_num < k:
                l = l + 1

        return ans
