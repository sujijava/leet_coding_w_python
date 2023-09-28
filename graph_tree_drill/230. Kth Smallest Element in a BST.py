#     3
#    / \
#   1   4
#    \
#     2
# k = 1
# Output: 1

# summary
# in order traversal

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.k = k
        self.res = None
        self.in_order(root)
        return self.res

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.counter = self.counter + 1
        if self.counter == self.k:
            self.res = root.val
            return
        self.in_order(root.right)
