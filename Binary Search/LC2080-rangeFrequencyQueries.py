class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.positions = [[] for _ in range(10001)]
        for i, val in enumerate(arr):
            self.positions[val].append(i)
    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.positions[value], right) - bisect_left(self.positions[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)