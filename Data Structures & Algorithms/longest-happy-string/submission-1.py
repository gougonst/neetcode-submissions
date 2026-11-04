class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        while len(heap) > 1:
            freq1, key1 = heapq.heappop(heap)
            freq2, key2 = heapq.heappop(heap)

            freq1 = -freq1
            freq2 = -freq2

            if freq1 - freq2 >= 2:
                res += key1 + key1 + key2
                freq1 -= 2
            else:
                res += key1 + key2
                freq1 -= 1
            freq2 -= 1

            if freq1 > 0:
                heapq.heappush(heap, (-freq1, key1))
            if freq2 > 0:
                heapq.heappush(heap, (-freq2, key2))

        if heap:
            freq = -heap[0][0]
            key = heap[0][1]
            res += key + key if freq >= 2 else key
        
        return res
