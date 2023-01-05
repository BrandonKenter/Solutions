class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            cur_h = 0
            for pile in piles:
                cur_h += math.ceil(pile / mid)
            if cur_h <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1
        return k