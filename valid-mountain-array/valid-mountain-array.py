class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:                                    # if length is less than 3 no mountain can be structured
            return False
        
        i=1                                                 # start from index 1
        
        while(i < len(arr) and arr[i] > arr[i-1]):          # loop from 1 to end of array & check for rising structure of mountain  
            i+=1                                            # by checking if current value > previous value
            
        if i == 1 or i == len(arr):                         #if there's no rise then return false
            return False
        
        while(i < len(arr) and arr[i] < arr[i-1]):          # now check for decreasing structure of mountain
            i+=1                                            # by comparing current value < previous value
        
        return i==len(arr)                                  # return TRUE if condition is satisfied
        