class Solution:
    def maxPower(self, s: str) -> int:
        max_consec, left = 1, 0
    
        for right in range(len(s)):
            while s[left] != s[right]:
                left += 1
            max_consec = max(max_consec, right - left + 1)
        return max_consec
