class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start, end = intervals[0][0], intervals[0][1]

        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                ans.append([start, end])
                start = intervals[i][0]

            end = max(end, intervals[i][1])
        ans.append([start, end])

        return ans