class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0 for x in range(m)] for y in range(n)] # create matrix filled with zeros m = rows and n = columns
        
        
        for i in range(m): # rows                     # set first rows values = 1
            dp[0][i] = 1
        
        for i in range(n): # columns                  # set first column values = 1
            dp[i][0] = 1
        
      
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]    # to find cell[1,1] = dp[0][1] + dp[1][0] i.e. add left value with up valu
        
        return dp[-1][-1]                             # we have to find the finish point so return last cells of dp