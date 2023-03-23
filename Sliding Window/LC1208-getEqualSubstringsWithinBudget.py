class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = maxi = cur = 0
        for right in range(len(s)):
            r_dif = abs(ord(s[right]) - ord(t[right]))
            cur += r_dif
            if cur <= maxCost:
                maxi = max(maxi, right - left + 1)
            else:
                while cur > maxCost:
                    l_dif = abs(ord(s[left]) - ord(t[left]))
                    cur -= l_dif
                    left += 1
        return maxi
        