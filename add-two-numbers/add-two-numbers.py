# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head1 = l1                              
        head2 = l2
        
        str1 = ''                                   # str1 collects all the values of head1 in reverse order
        str2 = ''                                   # str2 collects all the values of head2 in reverse order
        
        dummy = newNode = ListNode(0)               # creates ListNode with value 0 as first node value, important!
            
        while head1:                                # traversing first linked List 
            str1 =  str(head1.val) + str1           # store the value of linkedList in form of & strings in reverse order 
            head1 = head1.next                      # move head1 to collect remaining values
        
        while head2 is not None:                    # traversing second linked List
            str2 =  str(head2.val) + str2           # store the value of linkedList in form of & strings in reverse order 
            head2 = head2.next                      # move head1 to collect remaining values
        
        sum1 = str(int(str1)+int(str2))[::-1]       # convert the str1 and str2 to int and perform addition operation 
                                                    # and then store them back in form of string  in reverse order
                                                    # [::-1] used for storing in reverse order
        
        for i in sum1:                              # go through each character in string
            newNode.next = ListNode(val = int(i))   # this will do the following, newNode=(0) ->(character in integer format) 
            newNode = newNode.next                  # keep moving to insert all the characters of sum1 
        
        newNode.next = None                         # final node points to None. Marking end of linked List
        return dummy.next                           # dummy points to newNode's head, 
                                                    # note: returning dummy will include the first value too .i.e(0)
                                                    # so, for skipping first element return dummy.next 
        
        
        
