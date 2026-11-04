class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []

        maxHeap = []
        for i in range(k - 1):
            num = nums[i]
            heapq.heappush(maxHeap, (-num, i))

        for i in range(k - 1, len(nums)):
            num = nums[i]
            heapq.heappush(maxHeap, (-num, i))

            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)

            maxElements.append(-maxHeap[0][0])

        return maxElements