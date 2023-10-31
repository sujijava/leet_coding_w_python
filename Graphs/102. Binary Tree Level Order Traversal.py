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
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)

        while queue:
            size = len(queue)
            curr_level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_level)
        return res
