# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     3
#    / \
#   9  20
#     /  \
#    15   7
# ^^^ return True

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# ^^^ return False
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.check(root) != -1

    def check(self, node):
        if not node:
            return 0

        left = self.check(node.left)
        right = self.check(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1
