class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        # [0, 1, 2]
        # [50, 100, 200, 300]
        # [50, 100, 150, 300]
        # [50, 125, 150, 300]
        for i in range(k + 1):
            tmpPrices = prices.copy()
            for src, dest, price in flights:
                if prices[src] == math.inf:
                    continue
                if price + prices[src] < tmpPrices[dest]:
                    tmpPrices[dest] = price + prices[src]
            prices = tmpPrices
        return -1 if prices[dst] == math.inf else prices[dst]
                