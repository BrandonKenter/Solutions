class MedianFinder:
    def __init__(self):
        self.lower = [] # maxheap
        self.higher = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        
        if self.higher and self.higher[0] < -1 * self.lower[0]:
            heapq.heappush(self.higher, -1 * heapq.heappop(self.lower))
        if (len(self.lower) - len(self.higher)) > 1:
            heapq.heappush(self.higher, -1 * heapq.heappop(self.lower))
        if (len(self.higher) - len(self.lower)) > 1:
            heapq.heappush(self.lower, -1 * heapq.heappop(self.higher))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -1 * self.lower[0]
        elif len(self.higher) > len(self.lower):
            return self.higher[0]
        else:
            l = -1 * self.lower[0]
            h = self.higher[0]
            return (l + h) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()