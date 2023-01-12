class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_h = [-num for num in nums]
        heapq.heapify(max_h)
        score = 0

        for i in range(k):
            val = heapq.heappop(max_h)
            val *= -1
            score += val
            val = -1 * ceil(val / 3)
            heapq.heappush(max_h, val)
        return score