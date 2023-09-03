class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in map:
                return [i, diff[i]]
            else:
                num = nums[i]
                if map[num]:
                    map[num] = map[num] + 1
                else:
                    map[num] = 1
