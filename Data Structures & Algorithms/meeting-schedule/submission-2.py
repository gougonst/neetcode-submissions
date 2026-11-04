"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start))

        lastInterval = Interval(-1, -1)
        for interval in intervals:
            if interval.start < lastInterval.end:
                return False
            lastInterval = interval
        return True