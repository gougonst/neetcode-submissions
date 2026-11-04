class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = {}
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, freq in count.items():
            buckets[freq].append(num)

        topk = []
        for bucket in reversed(buckets):
            for num in bucket:
                topk.append(num)
                if len(topk) == k:
                    return topk
        return topk
