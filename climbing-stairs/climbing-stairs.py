class Solution:
    def climbStairs(self, n: int) -> int:
                                        # similar to fibonacci series
        
        if n == 1:                      # for faster execution
            return 1
        if n == 2:                      # for faster execution
            return 2
            
        dp = [0] * (n+1)                # create an extra cell space
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):         # considering the nth sequence too
            dp[i] = dp[i-1]+dp[i-2]     # dp[3] = dp[3-1] + dp[3-2] => dp[3] = dp[1] + dp[2] => dp[3] = 1 + 2  = 3
        return dp[n]                    # Similarly dp[4] = dp[3] + dp[2] => 3 + 2 = 5 ..... So on
        