'''
Add and then check
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_counts = defaultdict(int)
        longest = 0
        left = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1

            while len(char_counts) > 2:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    char_counts.pop(s[left])
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest


'''
Check before adding
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_counts = defaultdict(int)
        longest = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in char_counts:
                while len(char_counts) == 2:
                    char_counts[s[left]] -= 1
                    if char_counts[s[left]] == 0:
                        char_counts.pop(s[left])
                    left += 1
            
            char_counts[s[right]] += 1
            longest = max(longest, right - left + 1)
        return longest
