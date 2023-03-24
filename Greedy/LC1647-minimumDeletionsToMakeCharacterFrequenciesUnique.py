class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        c = sorted(counts.values(), reverse=True)
        deletions = 0
        for i in range(1, len(c)):
            prev, cur = c[i-1], c[i]
            if prev <= cur:
                if prev == 0:
                    c[i] = 0
                    deletions += cur
                else:
                    c[i] = prev - 1
                    deletions += cur - prev + 1
        return deletions
