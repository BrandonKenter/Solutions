'''
No intervals array
Use prev_s and prev_e to keep track of previous start/end coords
O(N) time / O(1) space
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev_s, prev_e = points[0]
        count = 1

        for i in range(1, len(points)):
            cur_s, cur_e = points[i]
            if cur_s > prev_e:
                prev_s, prev_e = points[i][0], points[i][1]
                count += 1
            else:
                prev_s = min(prev_s, cur_s)
                prev_e = min(prev_e, cur_e)
        return count

'''
Use intervals array
use intervals[-1] to keep track of previous start/end coords
O(N) time / O(N) space
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        intervals = [points[0]]

        for i in range(1, len(points)):
            prev_s, prev_e = intervals[-1]
            cur_s, cur_e = points[i]
            if cur_s > prev_e:
                intervals.append(points[i])
            else:
                intervals[-1][0] = min(prev_s, cur_s)
                intervals[-1][1] = min(prev_e, cur_e)
        return len(intervals)