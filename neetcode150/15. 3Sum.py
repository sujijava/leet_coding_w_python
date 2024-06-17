from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        res = []

        for l in range(len(nums)):
            # Skip duplicate elements for l
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m = l + 1
            r = len(nums) - 1

            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]
                if curr_sum == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    # Skip duplicate elements for m
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
                    # # Skip duplicate elements for r
                    # code actually works with or without it. WHY?
                    # while m < r and nums[r] == nums[r + 1]:
                    #     r -= 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    m += 1
        return res 
