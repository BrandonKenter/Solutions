class Solution:
    def maxPower(self, s: str) -> int:
        max_conseq, cur_char, left = 1, s[0], 0
    
        for right in range(len(s)):
            if s[right] == cur_char:
                max_conseq = max(max_conseq, right - left + 1)
            else:
                left = right
                cur_char = s[left]
        return max_conseq