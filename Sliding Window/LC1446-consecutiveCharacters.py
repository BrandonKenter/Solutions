class Solution:
    def maxPower(self, s: str) -> int:
        max_consec, cur_char, left = 1, s[0], 0
    
        for right in range(len(s)):
            if s[right] == cur_char:
                max_consec = max(max_consec, right - left + 1)
            else:
                left = right
                cur_char = s[left]
        return max_consec
