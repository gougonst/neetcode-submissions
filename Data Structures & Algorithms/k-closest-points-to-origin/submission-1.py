class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePQ = [(x ** 2 + y ** 2, [x, y]) 
                      for x, y in points]
        heapq.heapify(distancePQ)

        topK = []
        for _ in range(k):
            if not heapq:
                break
            topK.append(heapq.heappop(distancePQ)[1])
        return topK