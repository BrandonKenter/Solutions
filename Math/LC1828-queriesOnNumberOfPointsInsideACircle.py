class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        for i, query in enumerate(queries):
            cx, cy, r = query
            for point in points:
                x, y = point
                if sqrt((cx - x)**2 + (cy - y)**2) <= r:
                    res[i] += 1
        return res
