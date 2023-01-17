class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n+1)
        self.i = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        j = self.i
        if self.stream[self.i]:
            while self.stream[self.i]:
                self.i += 1
            return self.stream[j:self.i]
        else:
            return []



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)