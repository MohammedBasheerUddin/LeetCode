class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        len1 = len(nums)             #idea is to create a new temp array with distinct values of orignal nums array
        s1 = set(nums)               #find length of temp array and orignal nums array           
        len2 = len(s1)      
                                     #the length of temp will be < orignal nums array if duplicate exist in nums array.
                                     #if length of temp == orignal nums array then no duplicates & returns false
        if len1 == len2:
            return False 
        else:
            return True
        