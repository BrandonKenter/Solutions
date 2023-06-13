class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0
        for num in range(1, n + 1):
            for div in [3, 5, 7]:
                if num % div == 0:
                    s += num
                    break
        return s
        