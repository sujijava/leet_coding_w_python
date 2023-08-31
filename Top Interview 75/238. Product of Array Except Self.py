# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]



from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]
        right = [1]
        ans = []

        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])
        # left = [1, 1, 2, 6]

        for j in range(len(nums) - 1):
            reverse = len(nums) - 1 - j
            right.insert(0, right[len(right) - 1 - j] * nums[reverse])
        # right = [24, 12, 4, 1]
        
        for l in range(len(left)): 
            ans.append(left[l] * right[l])
        
        # print(right)
        return ans
s = Solution()
print(s.productExceptSelf([1,2,3,4]))