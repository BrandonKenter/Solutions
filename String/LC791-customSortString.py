class Solution:
    def customSortString(self, order: str, s: str) -> str:
        indices = defaultdict(int)
        for i, c in enumerate(order):
            indices[i] = c
        
        s_counts = Counter(s)
        res = []
        for _, char in sorted(indices.items()):
            if char in s_counts:
                res.append(char * s_counts[char])
                s_counts.pop(char)
        for char, count in s_counts.items():
            res.append(count * char)
        return "".join(res)
        