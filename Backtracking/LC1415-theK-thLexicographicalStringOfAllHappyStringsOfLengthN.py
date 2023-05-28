class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = 'abc'
        strs = []
        s = []

        def backtrack(i):
            if i == n + 1:
                strs.append("".join(s))
                return
            
            for char in letters:
                if len(s) == 0:
                    s.append(char)
                    backtrack(i+1)
                    s.pop()
                else:
                    if s[-1] == char:
                        continue
                    s.append(char)
                    backtrack(i+1)
                    s.pop()
        
        backtrack(1)
        if len(strs) >= k:
            return strs[k - 1]
        else:
            return ""
