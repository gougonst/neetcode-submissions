class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        numsCount = defaultdict(int)

        for num in nums:
            numsCount[num] += 1

        frequentList = []
        for _ in range(n):
            frequentList.append([])

        for num, freq in numsCount.items():
            frequentList[freq - 1].append(num)

        topk = []
        for numList in reversed(frequentList):
            for num in numList:
                topk.append(num)
            if len(topk) == k:
                break
        return topk
