"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for idx in range(1, len(intervals)):
            prev_end = intervals[idx - 1].end
            curr_start = intervals[idx].start
            if curr_start < prev_end:
                return False
        return True