class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        steps = 0
        for i in range(26):
            if counts[i] > 0: steps += counts[i]
        return steps