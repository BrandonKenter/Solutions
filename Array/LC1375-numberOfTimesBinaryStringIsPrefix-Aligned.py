class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        largest = flipCount = res = 0
        for i in flips:
            flipCount += 1
            largest = max(largest, i)
            if largest == flipCount:
                res += 1
        return res
