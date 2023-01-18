class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        char_counts = defaultdict(int)
        good_count = left = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1

            if right - left + 1 == 3:
                if len(char_counts) == 3:
                    good_count += 1
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    char_counts.pop(s[left])
                left += 1
        return good_count