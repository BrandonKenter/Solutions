class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            c = s[i-1]
            x = chr(ord(c) + int(s[i]))
            s[i] = x
        return "".join(s)