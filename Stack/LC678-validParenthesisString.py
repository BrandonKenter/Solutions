class Solution:
    def checkValidString(self, s: str) -> bool:
        opens, stars = [], []
        for i, c in enumerate(s):
            if c == '*': stars.append(i)
            elif c == '(': opens.append(i)
            else:
                if opens: opens.pop()
                elif stars: stars.pop()
                else: return False
        
        while opens and stars:
            if opens[-1] < stars[-1]:
                opens.pop()
                stars.pop()
            else:
                return False
        return len(opens) == 0
        