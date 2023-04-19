class Solution:        
    def primeRange(self,M,N):
        primes = [True for i in range(N + 1)]
        for i in range(2, int(math.sqrt(N)) + 1):
            if primes[i]:
                for j in range(i * i, N + 1, i):
                    primes[j] = False
        
        res = []
        for i in range(M, N + 1):
            if primes[i] and i != 1 == True: res.append(i)
        return res
