class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i, d = 0, len(s)
        res = []
        for j in range(len(s)):
            if s[j] == 'I':
                res.append(i)
                i += 1
            else:
                res.append(d)
                d -= 1
        if s[-1] == 'D': res.append(d)
        else: res.append(i)
        return res
        