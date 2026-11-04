class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        diffs = []
        for interval in intervals:
            diffs.append((interval[0], 1))
            diffs.append((interval[1], -1))
        diffs.sort(key=lambda x: (x[0], -x[1]))

        ans = []
        sum = 0
        start, end = 0, 0
        for diff in diffs:
            if sum == 0 and diff[1] == 1:
                start = diff[0]
            elif sum > 0 and sum + diff[1] == 0:
                end = diff[0]
                ans.append([start, end])
            sum += diff[1]
        return ans
