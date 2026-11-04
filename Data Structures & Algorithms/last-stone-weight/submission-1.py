class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            remain = abs(first - second)
            if remain > 0:
                heapq.heappush(maxHeap, -remain)
        return -maxHeap[0] if len(maxHeap) > 0 else 0