class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 0:
            if s[0] == '1': return True
            else: return False

        segments = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                segments += 1
                if segments == 2: return False
        return True
