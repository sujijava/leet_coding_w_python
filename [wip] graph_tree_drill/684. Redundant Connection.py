class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(node):
            while parent[node] != node:
                # follows the chain of parent-child relationships
                # until "node" becomes its own parent,
                # which signifies it is the root of the set.
                node = parent[node]
            return node

        def union(i, j):
            iRoot = find(i)
            jRoot = find(j)
            if iRoot != jRoot:
                parent[jRoot] = iRoot

        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            union(edge[0], edge[1])

        return None


'''
Summary 
1. It manages a 'parent' list, initializing each node as its own parent.
# edges = [[1,2],[1,3],[2,3]]
# parent = [0,1,2] >> we don't use 0. 


2. The 'parent' values change dynamically as iterations occur.
- After [1,2], 'parent' becomes [0,1,2], 
    - indicating a union of nodes 1 and 2 under the root 1.
- After, [1,3], 'parent' shifts to [0,1,1], 
    - signifying the union of nodes 1 and 3 under the root 1.
- During the [2,3] iteration, 
    - a cycle is detected when nodes 2 and 3 unite under the same root (1).
    - This indicates a redundant connection, resulting in the return of [2,3].
    - if find(edge[0]) == find(edge[1])
'''
