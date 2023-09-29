# Input: root = [2,1,3]
# Output: true
#    2
#  /  \
# 1   3
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -float('inf'), float('inf'))

    def helper(root, min_val, max_val):
        if not root:
            return True
        if root.val <= min_val:
            return False
        if root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
