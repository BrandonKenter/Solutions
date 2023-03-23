class Solution:
    def countHomogenous(self, s: str) -> int:
        count = left = 0
        for right in range(len(s)):
            if s[right] == s[left]:
                count += right - left + 1
            else:
                left = right
                count += 1
        return count % (10**9 + 7)
        