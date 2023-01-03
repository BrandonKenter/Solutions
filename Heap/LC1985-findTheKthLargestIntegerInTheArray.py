class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_h = []
        
        for num in nums:
            heapq.heappush(min_h, int(num))
            if len(min_h) > k:
                heapq.heappop(min_h)
        return str(heapq.heappop(min_h))