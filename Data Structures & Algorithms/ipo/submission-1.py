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
        for _ in range(k):
            while i < n and totalCapital >= capital[i]:
                heapq.heappush(maxHeap, -profits[i])
                i += 1
            
            if not maxHeap:
                break

            totalCapital += -heapq.heappop(maxHeap)

        return totalCapital