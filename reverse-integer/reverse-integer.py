class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0            # stores boolean value if < 0 stores True else false
        ans = 0
        
        if negative:
            x = x *- 1              # if int is negative turn it into positive 
            
        
        while x>0:
            rem = x % 10            # gives last digit from integer
            ans = ans * 10 + rem    # reverses the integer by storing last digit of orignal integer as first digit in ans
            x //= 10                # removes last digit from integer       
                          
            
        
        if negative : 
            ans = ans *- 1         # turn the reversed positive number to negative if negative = True    
        
        if ans > (2**31) or ans < (-2)**31:
            return 0
        
        return  ans
        