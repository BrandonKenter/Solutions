class HitCounter:

    def __init__(self):
        self.hit_q = deque()
        self.num_hits = 0

    def hit(self, timestamp: int) -> None:
        self.hit_q.append(timestamp)
        self.num_hits += 1

    def getHits(self, timestamp: int) -> int:
        while self.hit_q and self.hit_q[0] <= timestamp - 300:
            self.hit_q.popleft()
            self.num_hits -= 1
        return self.num_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)