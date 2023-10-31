class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        subtotal = 0
        ans

        for i in nums:
            total += i

        for j in nums:
            if total - j / 2 == subtotal:
                ans = j
            subtotal += j

        if ans:
            ans
        else:
            False
