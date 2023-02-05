class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0: return True
        intervals.sort()
        prev_start, prev_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end: return False
            prev_end = end
        return True