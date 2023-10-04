# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# [3, 4, 5, 1, 2]
#  l     m     r
#           l  r

# [4, 5, 1, 2, 3]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # If 'mid' is greater than 'right,'
            # it indicates that the pivot (minimum value)
            # must be to the right of 'mid.'
            if nums[mid] > nums[right]:  # mid ~ right: \ descending
                left = mid + 1
            else:  # mid ~ right: / ascending
                #  if 'mid' is less than or equal to 'right,'
                #  it implies that the pivot is at 'mid' or to its left.
                right = mid

        return nums[left]
