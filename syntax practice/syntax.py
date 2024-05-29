class Solution:
    def twoSum(self, nums, target):
        l, r = 0, len(nums)-1
        while l<r:
            currSum = nums[l] + nums[r]
            if currSum < target:
                r -= 1
            elif currSum > target:
                l += 1 
            else:
                return [l, r]
        
        
s = Solution()
s.twoSum([],0)