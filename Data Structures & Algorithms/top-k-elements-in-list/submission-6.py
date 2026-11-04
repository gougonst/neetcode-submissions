class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = defaultdict(int)
        for num in nums:
            freq[num] += 1

        return sorted(freq, key=freq.get, reverse=True)[:k]