class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        subString = s.split()               # split the string
        if(len(subString)<=0):              # empty sting return 0
            return 0
        else:           
            return len(subString[-1])       #calculate length of last subString or last word