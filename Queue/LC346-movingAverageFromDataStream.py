class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.size = size
        self.q_sum = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.q_sum += val
        if len(self.q) > self.size:
            self.q_sum -= self.q[0]
            self.q.popleft()
        return self.q_sum / len(self.q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)