class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                if num > minHeap[0]:
                    heapq.heappushpop(minHeap, num)
        return minHeap[0]