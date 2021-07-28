class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Math @ 3                     # consider orignal array = [2,2,1].
        arrSum = sum(nums)             # sum up all orignal array elements,if orignal array = [2,2,1] then arrSum = 5
        uniq = set(nums)               # add all the unique elements of orignal array into uniq 
        uniqSum = sum(uniq)            # sum up all unique elements and store in uniqSum ,if orignal array = [2,2,1] then uniqSum = 3
        return int((2*uniqSum)-arrSum) # ((2 * 3) - 5) returns 1 , if orignal array = [2,2,1] 