class Solution:
    def pivotInteger(self, n: int) -> int:
        right_sum = n * (n + 1) / 2
        left_sum = 0
        for i in range(n + 1):
            left_sum += i
            if left_sum == right_sum: return i
            right_sum -= i
        return -1