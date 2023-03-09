'''
O(Nlog(N)) time / O(N) space
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_s, prev_e = res[-1][0], res[-1][1]
            s, e = intervals[i]
            if s >= prev_s and e <= prev_e:
                continue
            elif prev_s >= s and prev_e <= e:
                res.pop()
                res.append(intervals[i])
            else:
                res.append(intervals[i])
        return len(res)


'''
O(Nlog(N)) time / O(1) space
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        prev_e = intervals[0][1]
        res = len(intervals)
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if e <= prev_e:
                res -= 1
            else:
                prev_e = e
        return res
