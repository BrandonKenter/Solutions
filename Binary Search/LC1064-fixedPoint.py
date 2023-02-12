class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        smallest, left, right = -1, 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = arr[mid]
            if val == mid:
                smallest = val
                right = mid - 1
            elif val < mid:
                left = mid + 1
            else:
                right = mid - 1
        return smallest