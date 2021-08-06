
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        temp = head                     # temp is used to traverse and find out total length or count of linked list
        new = head                      # new node is used to traverse till nth - 1 node
        
        if head==None:                  # if empty linked list return None
            return None
        
        length=0                        # keeps track count of nodes in linked list
        
        while temp:                     # go through each node of linked list
            length += 1                 # increment lenght of linked list
            temp = temp.next            
        
        m = length-n                    # consider length = 5 and n =2 then m = 5-2 , m = 3. It gives the nth-1 node location
         
        if m == 0:                      # if m = 0 return empty list
            head = head.next
            return head
        
        index=0                         # used to reach m
        
        while index < m-1:              # consider m = 3 then, index = 0,1,2 and loop is terminated 
            new = new.next              # move to next node
            index = index+1             # incerement index 
        new.next = new.next.next        # after loop is terminated or index > m-1 move new node ->next  to new node ->next ->next
        
        return head                     # head point to first node so return it for accessing all the nodes