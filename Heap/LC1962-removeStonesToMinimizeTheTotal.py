class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_h = [-p for p in piles]
        heapq.heapify(max_h)

        for i in range(k):
            val = heapq.heappop(max_h)
            val //= 2
            heapq.heappush(max_h, val)
        return sum([-p for p in max_h])