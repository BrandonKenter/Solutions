class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_counts = Counter(arr)
        distinct_count = 0
        for s in arr:
            if string_counts[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""