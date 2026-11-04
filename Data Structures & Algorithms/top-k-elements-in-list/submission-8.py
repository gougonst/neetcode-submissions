class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        topk: list[tuple(int, int)] = []
        for num, freq in count.items():
            heapq.heappush(topk, (freq, num))
            if len(topk) > k:
                heapq.heappop(topk)
        
        return [num for _, num in topk]