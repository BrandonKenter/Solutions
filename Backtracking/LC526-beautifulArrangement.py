class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        perm = []
        used = [False] * (n + 1)

        def backtrack(i):
            nonlocal count
            if i > n:
                count += 1
                return
            
            for j in range(1, n + 1):
                if used[j]:
                    continue

                if j % i == 0 or i % j == 0:
                    used[j] = True                
                    backtrack(i + 1)
                    used[j] = False
        
        backtrack(1)
        return count
