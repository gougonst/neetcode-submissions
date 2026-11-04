class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePQ = [(pow(point[0], 2) + pow(point[1], 2), point) 
                      for point in points]
        heapq.heapify(distancePQ)

        topK = []
        for _ in range(k):
            if not heapq:
                break
            topK.append(heapq.heappop(distancePQ)[1])
        return topK