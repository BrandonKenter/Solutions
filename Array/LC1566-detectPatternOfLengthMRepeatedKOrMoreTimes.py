class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m + 1):
            count, pattern = 0, arr[i:i+m]
            while arr[i:i+m] == pattern:
                count += 1
                if count == k:
                    return True
                i += m
        return False
        