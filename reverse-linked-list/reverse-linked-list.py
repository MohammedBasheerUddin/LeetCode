# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prevnode = None             # keep track of previous node from head node   
        while head is not None:     # traversing the linked list
            next = head.next        # keeps track of next node from head node
            head.next = prevnode    # reversing the link by pointing to previous node
            prevnode = head         # update the previous node to head as head will move to next node
            head = next             # moving head to next element or node
        return prevnode             # at the end, prevNode points to first node of the reversed Linked List
                                    # so it act as head for the reversed linked list.