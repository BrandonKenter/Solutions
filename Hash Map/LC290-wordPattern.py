class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        ps = {}
        sp = {}
        
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            if char in ps and ps[char] != word: return False
            if word in sp and sp[word] != char: return False
            ps[char] = word
            sp[word] = char
        return True