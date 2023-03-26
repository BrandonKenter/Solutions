class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s = 0
        def backtrack(i):
            nonlocal s
            if s == n:
                return True
            if s > n:
                return False
            
            for j in range(i, 15):
                take = False
                p = pow(3, j)
                if s + p <= n:
                    s += p
                    take = backtrack(j + 1)
                    s -= p
                skip =  backtrack(j + 1)
                return take or skip
        return backtrack(0)
        