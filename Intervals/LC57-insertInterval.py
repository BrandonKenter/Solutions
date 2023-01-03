class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        
        for i in range(len(intervals)):
            s, e = intervals[i]
            if newInterval[1] < s:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > e:
                out.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        out.append(newInterval)
        return out