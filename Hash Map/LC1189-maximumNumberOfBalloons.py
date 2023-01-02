class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_counts = Counter("balloon")
        t_counts = Counter(text)

        min_count = float('inf')
        for b_char, b_count in b_counts.items():
            t_count = t_counts[b_char] // b_counts[b_char]
            min_count = min(min_count, t_count)
        return min_count