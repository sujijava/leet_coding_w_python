# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Bottom up
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        current_node = root
        while current_node is not None:
            if current_node.val == val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            elif val >= current_node.val:
                current_node = current_node.right

        return None

# Top down recursive approach
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if root is None:
#             return None

#         if val == root.val:
#             return root
#         elif val < root.val:
#             return self.searchBST(root.left, val)
#         else:
#             return self.searchBST(root.right, val)
