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


# python debugging code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Create nodes for the binary tree
node10 = TreeNode(10)
node5 = TreeNode(5)
node_minus3 = TreeNode(-3)
node3 = TreeNode(3)
node2 = TreeNode(2)
node11 = TreeNode(11)
node3_2 = TreeNode(3)
node_minus2 = TreeNode(-2)
node1 = TreeNode(1)

# Connect the nodes to form the binary tree
# node10.left = node5
# node10.right = node_minus3
# node5.left = node3
# node5.right = node2
# node_minus3.right = node11
# node3.left = node3_2
# node3.right = node_minus2
# node2.right = node1

# class Solution(object):
#     def pathSum(self, root, target):
#         self.result = 0
#         self.cache = {0: 1}  # Initialize with 0:1
#         self.dfs(root, target, 0)
#         return self.result

#     def dfs(self, root, target, current_sum):
#         if root is None:
#             return
#         current_sum = current_sum + root.val
#         prefix_needed = current_sum - target  # Calculate prefix_needed correctly
#         if prefix_needed in self.cache:
#             self.result += self.cache[prefix_needed]
#         self.cache[current_sum] = self.cache.get(current_sum, 0) + 1

#         self.dfs(root.left, target, current_sum)
#         self.dfs(root.right, target, current_sum)
#         # Remove current_sum from cache when backtracking
#         self.cache[current_sum] -= 1

# s = Solution()
# s.pathSum(node10, 8)
