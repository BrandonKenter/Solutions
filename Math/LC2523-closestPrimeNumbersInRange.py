class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for i in range(right + 1)]
        for i in range(2, int(sqrt(right)) + 1):
            if is_prime[i]:
                for j in range(i + i, right + 1, i):
                    is_prime[j] = False
        
        prev = -1
        res = [-1, -1]
        mini = float('inf')
        for i in range(2, right + 1):
            if left <= i <= right:
                if is_prime[i]:
                    if prev != -1:
                        length = i - prev + 1
                        if length < mini:
                            mini = length
                            res = [prev, i]
                    prev = i
        return res
