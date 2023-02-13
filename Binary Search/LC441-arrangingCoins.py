# Template 2
# Same as Sqrt(x)
# Find minimal k where isCondition(k) is True
# isCondition is "if coins > n"
# F F T T T T T <- find first index that is TRUE
# The first T in this problem means coins > n
# So the k to the left of it is when coins <= n
# It has to contain the ith coin due to our updating rules
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        # max k that satisfies condition(k)
        while left < right:
            mid = left + (right - left) // 2
            coins = (mid*(mid+1)) / 2
            # Update right until it is the first row k that has a sum of
            # coins >= n. So on the last update, left will equal right 
            # and we can return left - 1, which wil be the row that 
            # contains the nth coin.
            if coins > n:
                right = mid
            else:
                left = mid + 1
        return left - 1 if n != 1 else 1


# Template 1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, res = 0, n, 0
        
        while left <= right:
            mid = (left + right) // 2
            coins = (mid*(mid+1)) / 2
            if coins == n:
                return mid
            elif coins < n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
