class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        perm = []
        used = [False for i in range(n+1)]

        def backtrack():
            nonlocal count
            if len(perm) == n:
                count += 1
                return
            
            for i in range(1, n+1):
                if used[i] == False:
                    if i % (len(perm)+1) == 0 or (len(perm)+1) % i == 0:
                        used[i] = True
                        perm.append(i)
                        backtrack()
                        used[i] = False
                        perm.pop()
        
        backtrack()
        return count