# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast ahead by "n" steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return dummy.next
    
    
'''
Set the slow node n nodes behind the fast node. 
When fast reaches the end of the linked list, 
the slow node will be right before the node we want to remove. 
Adjust slow.next to skip the target node.
'''