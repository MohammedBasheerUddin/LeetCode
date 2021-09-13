class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        j = n - 1
        i = 0
        # logic replace first with last , next replace second with second last and so on....
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        
            
        
            
        