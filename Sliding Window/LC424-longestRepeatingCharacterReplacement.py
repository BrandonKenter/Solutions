class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        win_counts = defaultdict(int)
        l = 0
        
        for r in range(len(s)):
            win_counts[s[r]] += 1
            if (r - l + 1) - max(win_counts.values()) > k:
                win_counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest