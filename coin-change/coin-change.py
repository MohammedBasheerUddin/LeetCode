class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # idea is to find minimun no. of coins required at each stage
        # if given amount is 11 then we will find minimum coins required for 1,2,3,4,5..... 11
        # so that we can use this subproblem solution to build the required solution
        
        if amount <= 0:
            return 0
        
        if min(coins) > amount:
            return -1
        
        INT_MAX = 1<<32
        
        dp = [INT_MAX] * (amount+1)                         # initialize every cell of dp List as the maximum value possible
        
        dp[0] = 0                                           # the first cell intialized as zero
        
        for i in range(1, amount + 1):                      # if amt =11 ,we will find min coins required for all the amount from 1.....11+1
            for coin in coins:
                if coin <= i:                               # consider coin = 1,2,5 & i = 1...11 ,
                    dp[i] = min((dp[i-coin] + 1), dp[i])    # dp[1] = min(dp[i-1]+1, dp[i]) , here dp[i] = max value
                                                            # so dp[i-1]+1 = 0+1 here the + 1 indicates coin is added so dp[1] = 1
                                                            # dp[2] = min(dp[2-1]+1,dp[2]) = min(1+1,maxvalue) = 2, another possiblity is    
        return dp[amount] if dp[amount]!= INT_MAX else -1   # dp[2] = min (dp[2-2]+1),dp[20])= min(1,maxvalue) = 1, so dp[2] = 1