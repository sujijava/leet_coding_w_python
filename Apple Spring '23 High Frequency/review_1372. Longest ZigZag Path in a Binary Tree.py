# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0

        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    # This is to find another longest path from node.right
                    dfs(node.right, True, 1)
                else:
                    # This is to find another longest path from node.left
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.pathLength


s = Solution()


'''
Summary:
1. BFS 
    1) level by level
2. DFS 
    1) In order
    2) Pre order
    3) Post order 

Complexity:
 - Time: 
 - Space: 
'''
