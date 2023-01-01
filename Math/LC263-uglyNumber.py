class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for fact in [5, 3, 2]:
            while n % fact == 0:
                n = n // fact
        return n == 1