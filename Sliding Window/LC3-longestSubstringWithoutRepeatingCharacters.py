'''
Sliding Window - O(N) time / O(N) space
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        win = defaultdict(int)
        for r in range(len(s)):
            while s[r] in win:
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    win.pop(s[l])
                l += 1
            win[s[r]] += 1
            longest = max(longest, r - l + 1)
        return longest

'''
Check Every Substring - O(N^3) time / O(N) space
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                counts = Counter(s[i:j+1])
                if max(counts.values()) == 1:
                    longest = max(longest, j - i + 1)
        return longest
