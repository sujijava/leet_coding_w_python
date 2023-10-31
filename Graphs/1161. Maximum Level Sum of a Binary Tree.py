# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        curr_level = 0
        max_sum = -float('inf')
        res = 0

        while queue:
            level_size = len(queue)
            curr_sum = 0
            curr_level += 1
            for _ in range(level_size):
                curr = queue.popleft()
                curr_sum = curr_sum + curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if max_sum < curr_sum:
                max_sum = curr_sum
                res = curr_level

        return res
