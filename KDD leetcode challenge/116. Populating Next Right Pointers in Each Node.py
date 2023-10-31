from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q[0]
                q.remove(q[0])

                # the rightmost node does not have next
                if i < size - 1:
                    node.next = q[0]

                # BFS
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
