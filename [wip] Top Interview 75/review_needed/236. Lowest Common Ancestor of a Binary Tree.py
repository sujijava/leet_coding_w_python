# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     3
#    / \
#   5   1
#  / \ / \
# 6  2 0  8
#     / \
#    7   4

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if root == p or root == q:
            return root

        left = None
        right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
