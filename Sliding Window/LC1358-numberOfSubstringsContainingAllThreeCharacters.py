class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_counts = defaultdict(int)
        substr_count = left = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1

            while len(char_counts) == 3:
                char_counts[s[left]] -= 1
                if char_counts[s[left]] == 0:
                    char_counts.pop(s[left])
                left += 1
            substr_count += left
        return substr_count