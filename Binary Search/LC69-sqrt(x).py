# Template 2
# Find minimal k where isCondition(k) is True
# isCondition is "if mid * mid <= x"
# F F T T T T T <- find first index that is TRUE
# I think there can only be 2 T and we are looking for left T
#   because square root can only be an int or a floating point
#   number below the first number that takes mid * mid over
#   our target integer x.
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid  
            else:
                left = mid + 1
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
