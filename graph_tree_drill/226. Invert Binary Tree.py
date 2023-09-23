# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     4
#    / \
#   2   7
#  / \ / \
# 1  3 6  9

#      4
#     / \
#    7   2
#   / \ / \
#  9  6 3  1


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        left = root.left
        right = root.right

        root.left = right
        root.right = left
        self.invertTree(left)
        self.invertTree(right)
        return root
