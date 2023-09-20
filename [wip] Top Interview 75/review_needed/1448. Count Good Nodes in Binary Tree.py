
# Given a binary tree root, a node X in the tree is named good
# if in the path from root to X
# there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

#        3
#      /   \
#     1     4
#    /     / \
#   3     1   5
# Input: root = [3,1,4,3,null,1,5]
# Output: 4

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
