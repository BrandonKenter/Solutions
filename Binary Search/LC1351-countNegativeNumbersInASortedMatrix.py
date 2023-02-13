# Template 2
# Find minimal k where k < 0
# isCondition is "if arr[m] < 0"
# F F T T T T T <- find first index that is TRUE
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        for arr in grid:
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[m] < 0:
                    right = mid
                else:
                    left = mid + 1
            total += len(arr) - left 
        return total


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
