class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums)):
            if nums[l] > 0:
                break
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m = l + 1
            r = len(nums) - 1
            while m < r:
                curr_sum = nums[l] + nums[m] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
        return res
