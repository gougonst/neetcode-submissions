class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        end = intervals[0][0]
        count = 0
        for interval in intervals:
            if interval[0] < end:
                count += 1
                end = min(end, interval[1])
            else:
                end = interval[1]
        return count