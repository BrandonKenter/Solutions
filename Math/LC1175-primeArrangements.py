class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 2: return 1
        isPrime = [True] * (n+1)

        for i in range(2, floor(sqrt(n))+1):
            if isPrime[i]:
                j = i
                while j + i <= n:
                    isPrime[j + i] = False
                    j += i

        numPrimes = 0
        for i in range(2, n+1):
            if isPrime[i]:
                numPrimes += 1
        return (factorial(n - numPrimes) * factorial(numPrimes)) % (10**9 + 7)
