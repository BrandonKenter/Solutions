class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        
        for count in counts.values():
            length += count // 2 * 2
        if length < len(s): length += 1
        return length