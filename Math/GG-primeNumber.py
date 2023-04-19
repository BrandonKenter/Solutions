class Solution:
    def isPrime (self, N):
        if N == 1: return 0
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0: return 0
        return 1
    