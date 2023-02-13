# Template 1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, res = 0, n, 0
        
        while l <= r:
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


# Template 2
# Same as Sqrt(x)
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        # max k that satisfies condition(k)
        while left < right:
            mid = (left + right) // 2
            coins = (mid*(mid+1)) / 2
            if coins <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1 if n != 1 else 1
