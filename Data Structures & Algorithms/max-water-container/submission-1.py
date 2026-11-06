class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max(min(heights[l], heights[r]) * (r - l))
        l, r = 0, len(heights) - 1
        maxVal = 0
        while l < r:
            maxVal = max(maxVal, min(heights[l], heights[r]) * (r - l))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return maxVal
