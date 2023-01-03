class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = 'balloon'
        t_counts = defaultdict(int)
        for t in text:
            if t in b:
                t_counts[t] += 1
        
        b_counts = Counter('balloon')
        for c, count in b_counts.items():
            t_counts[c] = t_counts[c] // count
        return min(t_counts.values())