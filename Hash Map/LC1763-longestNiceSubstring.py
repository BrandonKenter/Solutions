class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = 0
        longest_indices = [-1, -1]
        for i in range(len(s) - 1):
            for j in range(i, len(s)):
                substr_set = set(s[i:j+1])
                nice = True
                for k in range(26):
                    upper = chr(ord('a') + k)
                    lower = chr(ord('A') + k)
                    if lower in substr_set and upper not in substr_set:
                        nice = False
                        break
                    if upper in substr_set and lower not in substr_set:
                        nice = False
                        break
                if nice:
                    if j - i + 1 > longest:
                        longest = j - i + 1
                        longest_indices = [i, j]

        i, j = longest_indices
        return s[i:j+1] if longest != 0 else ""