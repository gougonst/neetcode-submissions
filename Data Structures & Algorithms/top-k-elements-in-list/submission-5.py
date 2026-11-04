class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq: dict[int, int] = defaultdict(int)
        for num in nums:
            freq[num] += 1

        sortedFreq = sorted(freq.items(), key=lambda item: -item[1])
        return [n for n, _ in sortedFreq][:k]