# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


        # 1
        #  \
        #   1
        #  / \
        # 1   1
        #    /
        #   1
        #  /
        # 1
class Solution(object):
    def longestZigZag(self, root):
        self.max_length = 0
        self.dfs(root, "left", 0)
        self.dfs(root, "right", 0)
        return self.max_length

    def dfs(self, root, direction, length):
        if root is None:
            return
        self.max_length = max(self.max_length, length)
        if direction == "left":
            self.dfs(root.left, "right", length + 1)
            self.dfs(root.right, "left", 1)
        else:
            self.dfs(root.left, "right", 1)
            self.dfs(root.right, "left", length + 1)
