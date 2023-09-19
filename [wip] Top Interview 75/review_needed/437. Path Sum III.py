#          10
#         /  \
#        5   -3
#       / \    \
#      3   2   11
#     / \   \
#    3  -2   1

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3

class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        self.cache = {0: 1}  # Initialize with 0:1
        self.dfs(root, target, 0)
        return self.result

    def dfs(self, root, target, current_sum):
        if root is None:
            return
        current_sum = current_sum + root.val
        prefix_needed = current_sum - target  # Calculate prefix_needed correctly
        if prefix_needed in self.cache:
            self.result += self.cache[prefix_needed]
        self.cache[current_sum] = self.cache.get(current_sum, 0) + 1

        self.dfs(root.left, target, current_sum)
        self.dfs(root.right, target, current_sum)
        # Remove current_sum from cache when backtracking
        self.cache[current_sum] -= 1
