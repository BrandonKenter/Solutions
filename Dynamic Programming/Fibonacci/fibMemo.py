class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n in memo: return memo[n]

        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]