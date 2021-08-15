class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount+1)                            # consider amount = 5 then create 6 cells of value = 0
        ways[0] = 1                                        # set first cell value = 1  
        for coin in coins:                                 # consider coins  = 1, 2, 5 ,
                                                           # first we will check how we can pay amount using only firstCoin followed by second coin .....
            for amt in range(amount+1):                    # if given amount is 5 then we loop till (0 to 5+1) i.e 7 times 
                if coin <= amt:                            # if true we will store the no. of ways the amount can be paid using diffrent combination of coins
                    ways[amt] = ways[amt] + ways[amt-coin] # ways[2] = ways[2] + ways[2-1] --> ways[2] = 1 In first iteration ! remember ways[2] is set to 0                                                              previously
                                                           # ways[3] = ways[3] + ways[3-1] --> ways[3] = 1 In first Iteration
        return ways[-1]