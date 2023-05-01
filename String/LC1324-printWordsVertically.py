class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        maxi = max([len(word) for word in s])
        
        res = []
        for c in range(maxi):
            word = []
            for r in range(len(s)):
                if c >= len(s[r]):
                    word.append(" ")
                else:
                    word.append(s[r][c])
            res.append("".join(word).rstrip())
        return res
        