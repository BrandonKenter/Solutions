# Template 2
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            # Finding the minimal k satisfying condition(k) = True
            # This is either the square root or the square root - 1
            # because it can be directly equal, or it will be a floating
            # point of the previous number, so it is rounded down.
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        # Since we are ending to the right (last op is left = mid + 1)
        # we return left - 1.
        return left - 1
        

# Template 1
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
