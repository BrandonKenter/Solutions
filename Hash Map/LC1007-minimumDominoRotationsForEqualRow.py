class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        uniques, t_counts, b_counts = defaultdict(int), defaultdict(int), defaultdict(int)
        for i in range(n):
            if tops[i] == bottoms[i]:
                uniques[tops[i]] += 1
            else:
                uniques[tops[i]] += 1
                uniques[bottoms[i]] += 1
            t_counts[tops[i]] += 1
            b_counts[bottoms[i]] += 1
        
        mini = float('inf')
        for val, uni_count in uniques.items():
            if uni_count == n:
                mini = min(mini, n - t_counts[val], n - b_counts[val])
        return mini if mini != float('inf') else -1
