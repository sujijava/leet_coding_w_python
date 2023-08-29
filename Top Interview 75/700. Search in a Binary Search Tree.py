# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.helper(root, val)

    def helper(self, root, val):
        if root == None:
            return None
        if root.val == val:
            return root
        # Recursively call helper on the left and right subtrees
        left_result = self.helper(root.left, val)
        right_result = self.helper(root.right, val)

        # Check if the value was found in either subtree
        if left_result:
            return left_result
        if right_result:
            return right_result

        return None
