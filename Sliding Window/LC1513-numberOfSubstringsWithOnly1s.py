class Solution:
    def numSub(self, s: str) -> int:
        count = left = 0
        for right in range(len(s)):
            if s[right] != '1':
                n = right - left
                count += n * (n+1) // 2
                left = right + 1
        if left <= len(s) - 1:
            n = len(s) - left
            count += n * (n+1) // 2
        return count % (10**9 + 7)
        