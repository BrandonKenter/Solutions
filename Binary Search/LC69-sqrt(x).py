class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x
            
        left, right = 1, x // 2
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res