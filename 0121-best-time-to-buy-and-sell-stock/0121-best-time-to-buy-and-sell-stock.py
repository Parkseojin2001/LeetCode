class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -sys.maxsize
        start = prices[0]
        for price in prices:
            if start > price:
                start = price
            if max_profit < price - start:
                max_profit = price - start
        return max_profit
            
