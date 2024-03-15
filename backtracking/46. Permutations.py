from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         # base case
#         if len(nums) == 1:
#             return [nums[:]]  # nums[:] is a deep copy

#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)

#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.append(n)
#         return res

# [1,2,3] ---> 
# []
# [1]
# [1,2] [2,1]
# [3,1,2] [1,3,2] [1,2,3] [3,2,1] [2,3,1] [2,1,3]

def permute(self, nums):
    perms = [[]]  # Initialize perms list with an empty list

    # Iterate through each number in nums
    for new_num in nums:
        curr_perm_count = len(perms)

        # popping out existing perms
        for _ in range(curr_perm_count):
            curr_perm = perms.pop(0)  

            # make new perm by adding 'new_num' to each curr_perm
            # 'new num' will be added to before and after each element
            # for example, if it is [1] -> [point, 1, point]
            #              if it is [1,2] -> [point, 1, point, 2, point]
            #              therefore len(curr_perm) + 1 
            new_num_appending_points = len(curr_perm) + 1
            for i in range(new_num_appending_points):
                new_perm = curr_perm[:]  # just copy
                new_perm.insert(i, new_num)  # append the 'num_num' at point i
                perms.append(new_perm)  # append the new perm to res

    return perms  # Return the list of all perms


s = Solution()
s.permute([1,2,3])