class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        lastEnd = intervals[0][0]
        count = 0
        for start, end in intervals:
            if start < lastEnd:
                count += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end
        return count