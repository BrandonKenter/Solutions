class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = ["" for i in range(len(s))]
        for word in s:
            idx = int(word[-1]) - 1
            res[idx] = word[:-1]
        return " ".join(res)