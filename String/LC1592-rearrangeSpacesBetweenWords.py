class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        for c in text: 
            if c == ' ': spaces += 1
        
        words = text.split()
        if len(words) == 1: return words[0] + (' ' * spaces)
        space_len = spaces // (len(words) - 1)
        remainder = spaces % (len(words) - 1)
        res = []
        for i in range(len(words) - 1):
            res.append(words[i] + ' ' * space_len)
        res.append(words[-1])
        if remainder:
            res.append(' ' * remainder)
        return "".join(res)
        