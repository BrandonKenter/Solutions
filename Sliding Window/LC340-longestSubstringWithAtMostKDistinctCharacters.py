class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        distinct = longest = left = 0
        for right in range(len(s)):
            if s[right] not in char_counts:
                distinct += 1
            char_counts[s[right]] += 1

            while len(char_counts) == k + 1:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    char_counts.pop(s[left])
                    distinct -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest