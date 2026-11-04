class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k

        # minimum heap with largest K elements
        heapq.heapify(self.heap)
        while k < len(self.heap):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        