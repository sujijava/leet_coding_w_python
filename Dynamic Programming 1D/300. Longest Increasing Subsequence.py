from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for n_idx in range(len(nums) - 1, -1, -1):
            for latter_n_idx in range(n_idx + 1, len(nums)):
                if nums[n_idx] < nums[latter_n_idx]:
                    LIS[n_idx] = max(LIS[n_idx], 1 + LIS[latter_n_idx])
        print(LIS)
        return max(LIS)

nums = [0,1,0,3,2,3]
# LIS = [4, 3, 3, 1, 2, 1]
s = Solution()
s.lengthOfLIS(nums)

'''
LIS = [4, 3, 3, 1, 2, 1]
LIS[0] = 4 
- the longest subsequence length that includes nums[0] is 4. 
- [0,1,2,3]

LIS[1] = 3 
- the longest subsequence length that includes nums[1] is 3. 
- [1,2,3]
'''