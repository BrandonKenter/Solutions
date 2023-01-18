class Solution:
    def digitCount(self, num: str) -> bool:
        num_counts = Counter(num)
        for i, n in enumerate(num):
            if num_counts[str(i)] != int(n):
                return False
        return True