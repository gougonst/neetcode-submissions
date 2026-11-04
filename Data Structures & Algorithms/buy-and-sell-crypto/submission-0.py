class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for price in prices:
            if price < buyPrice:
                buyPrice = price
            profit = max(profit, price - buyPrice)
        return profit
            
        

# 5 6 7 4 5 8
# p1         
# p2
# profit: 0

# p1
#   p2
# profit: 1

# p1  
#     p2
# profit: 2

#       p1
#       p2
# profit: 0

#       p1
#         p2
# profit: 1

#       p1
#           p2
# profit: 4
