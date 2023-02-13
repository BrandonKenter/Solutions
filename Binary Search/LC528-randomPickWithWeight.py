from random import random

# Template 2
# Find minimal k where condition(k) is True
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.pre_sums = [weight for weight in w]
        for i in range(1, len(w)):
            self.pre_sums[i] += self.pre_sums[i-1]

    def pickIndex(self) -> int:
        target = randint(1, self.pre_sums[-1])
        left, right = 0, len(self.pre_sums) - 1
        while left < right:
            mid = (left + right) // 2
            mid_sum = self.pre_sums[mid]
            if mid_sum >= target:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
