class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:                                        # if no houses then no amout can be robbed
            return 0
        
        dp = [0] * n                                    # create n cells of value = 0
        
        dp[0] = nums[0]                                 # dp will contain the intial value of nums list
        
        for i in range(1, n):       
            if i == 1:
                dp[i] = max(nums[0],nums[1])            # decide which house to start robbing either first one or second one based on money 
            else:
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])    # compare the values based on money which can be robbed and store the max one
        
        
        return dp[n-1]                                  # the last value of dp contains max money