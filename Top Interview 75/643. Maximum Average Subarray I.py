# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        max_sum = curr_sum

        for i in range(k, len(nums)):
            add = nums[i]
            delete = nums[i-k]
            curr_sum = curr_sum + add - delete
            max_sum = max(curr_sum, max_sum)

        return max_sum/1.0/k
