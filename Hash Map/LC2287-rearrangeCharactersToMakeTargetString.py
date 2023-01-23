class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)
        min_count = float('inf')

        for t_char, t_count in target_counts.items():
            min_count = min(min_count, s_counts[t_char] // t_count)
        return min_count