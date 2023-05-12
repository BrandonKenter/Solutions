class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        cur = []

        def backtrack():
            if len(cur) == n:
                res.append(int("".join(cur)))
                return
            
            for i in range(10):
                if len(cur) == 0:
                    if i == 0:
                        continue
                    cur.append(str(i))
                    backtrack()
                    cur.pop()
                else:
                    if abs(int(cur[-1]) - i) != k:
                        continue
                    cur.append(str(i))
                    backtrack()
                    cur.pop()
        
        backtrack()
        return res