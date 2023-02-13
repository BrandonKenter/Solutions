# Template 2
# Find minimal k where isCondition(k) is True
# isCondition is "if k bananas/hour can eat all bananas"
# F F T T T T T <- find first index that is TRUE
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = len(piles)
        left, right = 1, max(piles)

        while left < right:
            cur_k = left + (right - left) // 2
            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile / cur_k)
            if cur_h <= h:
                right = cur_k
            else:
                left = cur_k + 1
        return left


# Template 1
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = len(piles)
        left, right = 1, max(piles)

        while left <= right:
            cur_k = left + (right - left) // 2
            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile / cur_k)
            if cur_h > h:
                left = cur_k + 1
            else:
                min_k = cur_k
                right = cur_k - 1
        return min_k
