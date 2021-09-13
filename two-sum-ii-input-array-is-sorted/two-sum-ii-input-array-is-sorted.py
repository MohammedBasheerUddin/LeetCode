class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers)-1
        
        while l <= h:
            if numbers[l]+numbers[h] ==  target:    # make combinations of first number with last number as array is sorted
                return [l+1,h+1]
            elif numbers[l]+numbers[h] > target:    # if combined value is > than target then decrement last pointer
                h = h - 1   
            else:                                   # if combined value is < than target the increment first pointer
                l += 1
        
        