class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        sortedNums = sorted(nums, reverse=True)

        # minimum heap with largest K elements
        self.heap = sortedNums[:k]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
