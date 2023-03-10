class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = ord('a') + int(s[i-2:i]) - 1
                char = chr(num)
                res.append(char)
                i -= 3
            else:
                num = ord('a') + int(s[i]) - 1
                char = chr(num)
                res.append(char)
                i -= 1
        return "".join(res[::-1])