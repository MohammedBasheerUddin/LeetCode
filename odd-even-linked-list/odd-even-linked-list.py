# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:                        # if linkedlist is empty return it
            return head
                                            # consider the linked list as, 1->2->3->4->5
        odd = head                          # odd is the first element of the linked list .i.e (1)
        even = odd.next                     # even is the second element of the linked list .i.e (2)
        evenList = even                     # this will keep track of the even value nodes (2->4)
        
        while even and even.next is not None:   # we will break from the loop if even or even.next is None
                                                # after seprating both even and odd list we break from the list
            odd.next = even.next                # the next odd element can be founded where even node next points
            odd = odd.next                      # move odd i.e odd head to next odd no.
            
            
            even.next = odd.next                # the next even element can be founded where odd node next points
            even = even.next                    # move even i.e even head to next even no.
            
        odd.next = evenList                     # connect the odd list with evenlist i.e. 1-3-5-2-4 first all odd values followed by even values
        
        return head                             # head points to first node so returning it will return whole list