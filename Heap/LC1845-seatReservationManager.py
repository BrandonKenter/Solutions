class SeatManager:

    def __init__(self, n: int):
        self.reserved = [0] * (n + 1)
        self.avail = [i for i in range(1, n + 1)] # min heap

    def reserve(self) -> int:
        smallest_seat = heapq.heappop(self.avail)
        self.reserved[smallest_seat] = 1
        return smallest_seat

    def unreserve(self, seatNumber: int) -> None:
        self.reserved[seatNumber] = 0
        heapq.heappush(self.avail, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)