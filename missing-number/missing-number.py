class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Math@1 
        currentSum = sum(nums)          # calculate sum of given array
        n = len(nums)          
        reqSum = (n*(n+1)/2)            # calculate the required sum by using  n*(n+1) / 2 gives intended sum
        
        return int(reqSum - currentSum) # return diffrence for finding missing number
    