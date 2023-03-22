class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widest = 0
        for i in range(len(points) - 1):
            width = points[i+1][0] - points[i][0]
            widest = max(widest, width)
        return widest
        