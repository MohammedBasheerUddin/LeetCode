class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        z = []
        if target not in nums:
            return [-1,-1]
        for i in range(0,len(nums)):
            if nums[i] == target:
                z.append(i)
#                 nums[i] = 0
#                 print(nums)
            
                
#                 self.searchRange(nums,target)
                
        z= [z[0],z[-1]]
        return z