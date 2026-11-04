"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        diffs = []
        for interval in intervals:
            diffs.append((interval.start, 1))
            diffs.append((interval.end, -1))
        diffs.sort()

        maxInterval = 0
        sum = 0
        for diff in diffs:
            sum += diff[1]
            maxInterval = max(maxInterval, sum)
        return maxInterval