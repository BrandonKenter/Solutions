class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        uniques = set(counts.values())
        return len(counts) == len(uniques)