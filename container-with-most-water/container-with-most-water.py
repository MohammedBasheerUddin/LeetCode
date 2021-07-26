class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # [1,8,6,2,5,4,8,3,7] array used for explaination
        # using two pointers for keeping track of water
        # store max water that can be stored and gets updated when finded maximum value
        maxarea = 0
        l = 0
        r = len(height)-1
        while(l<r):
            # maxarea = max(0, min(1,7)*(8)) => max(0, 1*8)
            maxarea = max(maxarea, min(height[l],height[r])*(r-l)) 
            
            if(height[l]<height[r]):     # actual array values are compared based on index and index values are incremented or
                l+=1                     # decremented based on condition satisfaction
            else:
                r-=1
                
        return maxarea
