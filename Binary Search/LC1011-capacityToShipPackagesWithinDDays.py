class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            cur_d, cur_w = 1, 0
            for w in weights:
                cur_w += w
                if cur_w > mid:
                    cur_d += 1
                    cur_w = w

            if cur_d <= days:
                right = mid
            else:
                left = mid + 1
        return left
