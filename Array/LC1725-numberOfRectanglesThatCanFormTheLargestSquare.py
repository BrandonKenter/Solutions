class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = 0
        for l, w in rectangles:
            max_len = max(max_len, min(l, w))
        
        count = 0
        for l, w in rectangles:
            if max_len <= min(l, w): count += 1
        return count