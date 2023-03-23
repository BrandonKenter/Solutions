class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_h = [-a, -b, -c]
        heapify(max_h)
        count = 0
        while len(max_h) >= 2:
            s1, s2 = heappop(max_h), heappop(max_h)
            s1, s2, count = s1 + 1, s2 + 1, count + 1
            if s1: heappush(max_h, s1)
            if s2: heappush(max_h, s2)
        return count
