class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_e = res[-1][1]
            s, e = intervals[i]
            if s <= prev_e:
                res[-1][1] = max(prev_e, e)
            else:
                res.append(intervals[i])
        return res