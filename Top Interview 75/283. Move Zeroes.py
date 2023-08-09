from ast import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        no_zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[no_zeros], nums[i] = nums[i], nums[no_zeros]
                no_zeros = no_zeros + 1
        return nums
