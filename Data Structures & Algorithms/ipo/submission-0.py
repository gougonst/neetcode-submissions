class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        combined = sorted(zip(capital, profits))
        if not combined:
            return w
        capital, profits = zip(*combined)

        maxHeap = []
        totalCapital = w
        
        n = len(profits)
        i = 0
        curk = 0
        while curk < k and i < n and totalCapital >= capital[i]:
            while i < n and totalCapital >= capital[i]:
                heapq.heappush(maxHeap, -profits[i])
                i += 1
            
            nextCapital = math.inf if i == n else capital[i]
            while maxHeap and totalCapital < nextCapital and curk < k:
                totalCapital += -heapq.heappop(maxHeap)
                curk += 1

        return totalCapital