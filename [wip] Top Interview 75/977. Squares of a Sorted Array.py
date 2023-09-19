# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []

        while left < right:  # equal
            if abs(nums[left]) < abs(nums[right]):
                ans.insert(0, nums[right] * nums[right])
                right = right - 1
            else:
                ans.insert(0, nums[left] * nums[left])
                left = left + 1

        return ans
