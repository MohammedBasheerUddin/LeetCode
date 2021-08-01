# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1                                    # to traverse elements 
        head2 = l2                                    # to traverse elements 
        
        sorted_listNode = ListNode(0)                 # create a ListNode structure for new variable sorted_listNode
        head = sorted_listNode                        # store the final array  
        
        while head1 and head2:                        # traverse through both heads
            if head1.val < head2.val:                 # compare head values so that elements are sorted during appending elements in sorted_listNodes
                sorted_listNode.next = head1          # set sorted_listNode -> head1
                head1 = head1.next                    # only move head1 if head1.val < head2.val
            else:
                sorted_listNode.next = head2          # set sorted_listNode -> head2
                head2 = head2.next                    # only move head2 if head2.val < head1.val
            sorted_listNode = sorted_listNode.next    # keep moving sorted+listNode to next 
        
        if head1 is None:                             # if head1 contain no values
            sorted_listNode.next = head2              # sorted_listNode points to head 2 as it already contains sorted values no need to sort again
        else:                                         # if head2 contain no values                  
            sorted_listNode.next = head1              # sorted_listNode points to head 1 as it already contains sorted values no need to sort again
        return head.next                              # returns the merged sorted lists