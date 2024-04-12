class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0 
        for n in nums:
            if n < 0:
                negatives += 1
            elif n == 0:
                return 0 
        if negatives % 2 == 0:
            return 1
        else:
            return -1
