'''
Use for loop to catch invalid states outside of constraints
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, combo = [], []
        
        def backtrack(prev):
            if len(combo) == k:
                res.append(combo[:])
                return
            
            for i in range(prev + 1, n + 1):
                combo.append(i)
                backtrack(i)
                combo.pop()
        backtrack(0)
        return res


'''
Use base cases to catch invalid states outside of constraints
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out, combo = [], []
        
        def backtrack(prev):
            if prev == n and len(combo) == k:
                out.append(combo[:])
                return
            if prev == n or len(combo) == k + 1:
                return
            
            combo.append(prev + 1)
            backtrack(prev + 1)
            combo.pop()
            backtrack(prev + 1)
        backtrack(0)
        return out