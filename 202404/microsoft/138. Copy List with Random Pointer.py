"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copies = {}
        curr = head 
        
        # map accepts Object as "Key" 
        # creating node without any relations
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy_curr = copies[curr]
            copy_curr.next = copies.get(curr.next) # copies[curr.next] is key error if not exists
            copy_curr.random = copies.get(curr.random)
            curr = curr.next 

        return copies[head]
        
        '''
        summary 
        I wanna know the interweaving too'''
