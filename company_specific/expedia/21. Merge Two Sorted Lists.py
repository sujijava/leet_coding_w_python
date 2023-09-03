# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        # Introduced a dummy node to keep track of the head of the merged list.
        dummy = ListNode(-1)
        # Using current to attach new nodes, while dummy stays at the start.
        current = dummy

        while one is not None and two is not None:
            if one.val <= two.val:
                current.next = one  # Changed head.next to current.next
                one = one.next
            else:
                current.next = two  # Changed head.next to current.next
                two = two.next
            # Move current to its next after attaching a node.
            current = current.next

        # Added this to handle when one of the lists is not fully consumed.
        if one:
            current.next = one
        if two:
            current.next = two

        # Returning the merged list starting after the dummy node.
        return dummy.next
