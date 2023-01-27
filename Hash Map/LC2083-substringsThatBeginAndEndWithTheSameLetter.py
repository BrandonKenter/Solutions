class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_counts = defaultdict(int)
        sub_count = 0
        for char in s:
            char_counts[char] += 1
            sub_count += char_counts[char]
        return sub_count