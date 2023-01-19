class Solution:
    def greatestLetter(self, s: str) -> str:
        char_set = set(s)
        upper, lower = ord('Z'), ord('z')
        for i in range(26):
            if chr(upper - i) in char_set and chr(lower - i) in char_set:
                return chr(upper - i)
        return ""