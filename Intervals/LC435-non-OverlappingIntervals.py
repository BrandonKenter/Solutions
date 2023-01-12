class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_e = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < prev_e:
                prev_e = min(prev_e, e)
                count += 1
            else:
                prev_e = e
        return count