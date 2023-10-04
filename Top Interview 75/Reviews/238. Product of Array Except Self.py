# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution(object):
    def productExceptSelf(self, nums):
        left = [1]  # [1,1,2,6]
        right = [1]  # [24,12,4,1]
        ans = []

        for i in range(len(nums)):
            left.append(left[i] * nums[i])

        for j in range(len(nums)):
            reverse = len(nums) - 1 - j
            right.insert(0, right[j] * nums[reverse])

        for l in range(len(left)):
            ans.append(left[i] * right[i])

        return ans
