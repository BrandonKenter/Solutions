class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        re_start, re_end = toBeRemoved
        res = []
        for start, end in intervals:
            if end <= re_start or start >= re_end: # Interval is before or after toBeRemoved
                res.append([start, end])
            elif start < re_start and end <= re_end: # Interval overlaps start of toBeRemoved
                res.append([start, re_start])
            elif start < re_start and end > re_end: # Interval overlaps entire toBeRemoved
                res.append([start, re_start])
                res.append([re_end, end])
            elif start >= re_start and end > re_end: # Interval overlaps end of toBeRemoved
                res.append([re_end, end])
            else: # Interval is overlapped by re_start and re_end (copmletely remove this interval)
                continue
        return res
