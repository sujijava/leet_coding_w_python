"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        node_map = {}

        def dfs(node):
            if node.val in node_map:
                return node_map[node.val]

            copy = Node(node.val)
            node_map[node.val] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None
