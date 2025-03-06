class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += prices[sell] - prices[buy]
            
            sell += 1
            buy += 1
        
        return profit
        

            

            
