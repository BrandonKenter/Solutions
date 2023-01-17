class Solution:
    def sortString(self, s: str) -> str:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        
        res = []
        while len(res) != len(s):
            for i in range(len(counts)):
                if counts[i] > 0:
                    char = chr(i + ord('a'))
                    res.append(char)
                    counts[i] -= 1
            for i in range(len(counts) - 1, -1, -1):
                if counts[i] > 0:
                    res.append(chr(i + ord('a')))
                    counts[i] -= 1
        return ''.join(res)