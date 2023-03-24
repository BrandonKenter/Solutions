class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num_primes = 0
        for i in range(2, n + 1):
            if self.is_prime(i):
                num_primes += 1
        return (factorial(n - num_primes) * factorial(num_primes)) % (10**9 + 7)

    def is_prime(self, num):
        for i in range(2, floor(sqrt(num)) + 1):
            if num % i == 0 and i != num:
                return False
        return True
