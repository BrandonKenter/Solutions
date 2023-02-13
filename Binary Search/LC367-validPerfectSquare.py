# Template 1
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
