class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        primes = [True for i in range(n)]
        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return primes[2:].count(True)
