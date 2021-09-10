class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        if target > max(nums):              # this will return index at last position
            return n
        if target < min(nums):              # this will return index of first position
            return 0
        
        low = 0
        high = n - 1
        
        while low <= high:
            mid = (low+high) // 2
            
            if target == nums[mid]:         # if the value is founded, then return the index of founded element
                return mid  
            
            if target > nums[mid]:          # if value to be founded is larger, then move low pointer to next element
                low += 1
            else:
                high -= 1                   # if value to found is smaller, then move high pointer to previous element
                
        return low                          # eventually low will give the answer if element to be founded is not present in orignal nums List
        
        
       
            