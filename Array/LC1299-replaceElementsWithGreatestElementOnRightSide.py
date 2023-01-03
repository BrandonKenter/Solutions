class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        m = arr[n - 1]
        if n == 1: return [-1]
        
        for i in range(n - 2, -1, -1):
            new_m = max(m, arr[i])
            arr[i] = m
            m = new_m
        arr[n - 1] = -1
        return arr