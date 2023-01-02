class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = [-s for s in stones]
        heapq.heapify(maxH)
        
        while len(maxH) > 1:
            s1 = heapq.heappop(maxH)
            s2 = heapq.heappop(maxH)
            if s1 < s2:
                heapq.heappush(maxH, s1 - s2)
        return -1 * heapq.heappop(maxH) if maxH else 0