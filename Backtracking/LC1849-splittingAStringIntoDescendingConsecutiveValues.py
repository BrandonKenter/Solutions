class Solution:
    def splitString(self, s: str) -> bool:
        values = []

        def backtrack(i):
            if i == len(s) and len(values) >= 2:
                return True
            elif i == len(s):
                return False
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if len(values) == 0 or int(sub) == values[-1] - 1:
                    values.append(int(sub))
                    if backtrack(j+1):
                        return True
                    values.pop()
            return False
        return backtrack(0)
        