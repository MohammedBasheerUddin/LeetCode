class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = max(prices) + (1)                 # set the buyPrice as max value of prices + 1 initially
        profit = 0                                   # set profit = 0
        for price in prices:                         # go through each price 
            if buyPrice > price:                     # as buyPrice is greater than any value of prices initially.  
                buyPrice = price                     # condition becomes true and buyPrice is updated to next lower price
            else:
                profit = max(profit, price-buyPrice) # if buyPrice is smaller than price calculate the profit that can be generated
        return profit                                # return the total profit after exiting the loop
                
        '''
          -> if prices = [7,1,5,3,6,4] then buyPrice will be = 8 initially, then we will go through each price of the prices List
          
          -> as buyPrice = 8 and price = 7 here buyPrice is greater than price so update the buyPrice = 7.Now go for the next price. 
          
          -> here buyPrice is > price update buyPrice = 1. Again go for the next price ,but now the buyPrice is not > price .i.e 1 > 5 = False
          
          -> So now we calculate the profit with max function max(profit, price-buyPrice) .i.e profit = max(0, 5-1), profit = 4. 
          
          -> The above steps are repeated until all the prices are evaluated.
        '''