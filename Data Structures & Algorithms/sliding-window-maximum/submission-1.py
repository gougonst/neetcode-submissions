class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # mono-decreasing queue

        maxElements = []

        window = collections.deque()

        for i, num in enumerate(nums):
            while window and num >= nums[window[-1]]:
                window.pop()
            window.append(i)

            while window and window[0] <= i - k:
                window.popleft()

            if i >= k - 1:
                maxElements.append(nums[window[0]])

        return maxElements