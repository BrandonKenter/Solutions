class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
        else:
            self.stream.append(num * self.stream[-1])

    def getProduct(self, k: int) -> int:
        i = len(self.stream) - 1 - k
        if i < 0:
            return 0
        else:
            return self.stream[-1] // self.stream[i]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)