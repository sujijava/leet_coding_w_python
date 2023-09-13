class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = nums[0]
        mid = nums[0]

        for num in nums:
            if num <= small:
                small = num
            elif num >= mid:
                mid = num
            else:
                return True

        return False
