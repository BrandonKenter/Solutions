class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        while fibs[-1] + fibs[-2] <= k:
            fibs.append(fibs[-1] + fibs[-2])
        ans = 0
        i = len(fibs) - 1
        while k != 0:
            ans += k // fibs[i]
            k %= fibs[i]
            i -= 1
        return ans
        