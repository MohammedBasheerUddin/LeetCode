class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=list(set(nums))        # keep unique values in s.
        l=len(nums)/2            # store length of nums // 2 ,to check majority within array.
        for i in s:              # go through only unique one . i.e the repeated ones or duplicate ones who stand a chance to win by majority.
            if nums.count(i)>l:  # check if thier count is greated than majority criteria.
                return i         # return the winner.
            

        
