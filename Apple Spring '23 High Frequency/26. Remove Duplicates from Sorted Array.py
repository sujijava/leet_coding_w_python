class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1

s = Solution()
print(s.removeDuplicates([1, 2, 2]))


'''
Summary:
i: unique char counter
j: explorer

Complexity:
 - Time: O(n)
 - Space: O(1)
'''
