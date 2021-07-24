class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxarea = 0
        l = 0
        r = len(height)-1
        while(l<r):
            maxarea = max(maxarea, min(height[l],height[r])*(r-l))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maxarea
    
#     class Solution:
#     def maxArea(self, height: List[int]) -> int:
         
#         # [1,8,6,2,5,4,8,3,7] array used for explaination
#         # using two pointers for keeping track of water
#         # store max water that can be stored and gets updated when finded maximum value 
#         maxarea = 0
#         l = 0 
#         r = len(height)-1
#         # go through each element 
#         while(l<r):
#             maxarea = max(maxarea, min(height[l],height[r])*(r-1)) 
#             #maxarea = max(0, min(1,7)*(8)) => max(0, 1*8)
#             if(height[l]<height[r]): # actual array values are compared based on index and index values are incremented or         
#                 l+=1                 # decremented based on condition satisfaction     
#             else:
#                 r-=1
#         return maxarea
