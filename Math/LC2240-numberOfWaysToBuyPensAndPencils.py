class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        cost1_total = 0
        while cost1_total <= total:
            ways += (total - cost1_total) // cost2 + 1
            cost1_total += cost1
        return ways
        