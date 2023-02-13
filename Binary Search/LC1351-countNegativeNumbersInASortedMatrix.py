# Template 1
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for arr in grid:
            l, r = 0, len(arr) - 1
            l_bound = -1
            while l <= r:
                m = (l + r) // 2
                if arr[m] < 0:
                    l_bound = m
                    r = m - 1
                else:
                    l = m + 1
            total += len(arr) - l_bound if l_bound != -1 else 0
        return total



# Template 2
# Find minimal k where k < 0
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for arr in grid:
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < 0:
                    r = m
                else:
                    l = m + 1
            total += len(arr) - l 
        return total
