class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        z = []                                     # store the occurences
        if target not in nums:                     # if targer not in array return [-1,-1] 
            return [-1,-1]
        for i in range(0,len(nums)):               # go through each element in array
            if nums[i] == target:                  # if target founded in array append its index in z
                z.append(i)                         
        z = [z[0],z[-1]]                           # return only first and last element of the z array
        return z                                   # return z .
