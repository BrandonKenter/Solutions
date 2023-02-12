from random import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sums = [weight for weight in w]
        for i in range(1, len(w)):
            self.sums[i] += self.sums[i-1]

    def pickIndex(self) -> int:
        rand = randint(1, self.sums[-1])
        left, right = 0, len(self.sums) - 1
        while left < right:
            mid = (left + right) // 2
            s = self.sums[mid]
            if s == rand:
                return mid
            elif s >= rand:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()