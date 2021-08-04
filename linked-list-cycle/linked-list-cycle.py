# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        hare = head                                 # consider the problem as competition between hare and turtle.   
        turtle = head                               # So both start at head which is a starting point for competition
            
        while turtle and hare and hare.next:        # if the list consists loop race will be infinite.
                                                    # and eventually hare and turtle will be at same point if loop/cycle exists
            hare = hare.next.next                   # hare hops two steps and turtle move only one step
            turtle = turtle.next                    
            if turtle == hare:                      # if both are at same point or position then linked list consists loop
                return True                         # so return True
        return False                                # else return False