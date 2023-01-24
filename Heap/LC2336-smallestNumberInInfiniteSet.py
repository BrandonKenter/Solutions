'''
Hash set + min heap
'''
class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = [i for i in range(1, 1001)]
        self.smallest_set = set([i for i in range(1, 1001)])

    def popSmallest(self) -> int:
        small = heapq.heappop(self.smallest)
        self.smallest_set.remove(small)
        return small

    def addBack(self, num: int) -> None:
        if num not in self.smallest_set:
            heapq.heappush(self.smallest, num)
            self.smallest_set.add(num)