class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        maxi = 0
        for word in s:
             maxi = max(maxi, len(word))
        for i in range(len(s)):
            s[i] = s[i] + " " * (maxi - len(s[i]))
        
        res = []
        for i in range(maxi):
            word = []
            for j in range(len(s)):
                word.append(s[j][i])
            w = "".join(word)
            w = w.rstrip()
            res.append(w)
        return res
        