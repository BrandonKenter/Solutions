# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Template 2
# Find minimal k where isBadVersion(k) is True
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Template 1
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
