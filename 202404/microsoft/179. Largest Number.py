from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return '0'
        # just checking if the array is valid i.e. does not contain 0, empty, ...
        
        nums = list(map(str, nums))
        # [3, 30, 34, 5, 9] -> ['3', '30', '34', '5', '9']
        
        if len(nums) < 2:
            return "".join(nums)
        
        def reverse_is_bigger(left, right):
            curr_sum = nums[left] + nums[right]
            reverse_sum = nums[right] + nums[left]
            return (int(curr_sum)) < (int(reverse_sum))
        
        for left in range(len(nums) - 1):
            for right in range(left+1, len(nums)):
                print(right)
                if reverse_is_bigger(left,right):
                    nums[right], nums[left] = nums[left], nums[right]
                
        return "".join(nums)

nums = [3,30,34,5,9]
s = Solution()
ans = s.largestNumber(nums)
print(ans)

'''
Summary
Sorting
- checking whether the reverse order or current order is bigger'''
