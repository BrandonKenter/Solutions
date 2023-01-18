class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_counts = Counter(target)
        arr_counts = Counter(arr)
        return target_counts == arr_counts