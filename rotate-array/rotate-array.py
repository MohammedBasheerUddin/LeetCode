class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # REMEMBER K CONDITION MAKES IT LIST CIRULAR
        if k>len(nums):
            k %= len(nums)
    
        
        nums[:] = nums[-k:] + nums[:-k]