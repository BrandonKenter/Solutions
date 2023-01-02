class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minH = nums
        heapq.heapify(nums)
        while len(self.minH) > k:
            heapq.heappop(self.minH)

    def add(self, val: int) -> int:
        heapq.heappush(self.minH, val)
        if len(self.minH) > self.k:
            heapq.heappop(self.minH)
        return self.minH[0]