# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodeCounter(root, root.val)

    def goodNodeCounter(self, node, max):
        # Check if the node is None, and return 0 if it is.
        if not node:
            return 0

        count = 0

        if node.val >= max:
            max = node.val
            count = count + 1

        left = self.goodNodeCounter(node.left, max)
        right = self.goodNodeCounter(node.right, max)

        return count + left + right


#        3
#      /   \
#     1     4
#    /     / \
#   3     1   5


# goodNodeCounter(3, 3)  # count = 4 (This is the total good nodes count)
# │
# ├── goodNodeCounter(1, 3)  # count = 1
# │   │
# │   └── goodNodeCounter(3, 3)  # count = 1 (3 >= 3)
# │
# └── goodNodeCounter(4, 3)  # count = 3
#     │
#     ├── goodNodeCounter(1, 4)  # count = 0 (1 < 4, so not counted)
#     │
#     └── goodNodeCounter(5, 4)  # count = 1 (5 >= 4)
