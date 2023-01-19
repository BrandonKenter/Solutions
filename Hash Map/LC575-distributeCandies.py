class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        type_counts = defaultdict(int)
        for t in candyType:
            type_counts[t] += 1
            
        return min(n // 2, len(type_counts))