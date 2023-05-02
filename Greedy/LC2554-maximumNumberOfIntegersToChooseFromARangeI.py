class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        b = set(banned)
        cnt = 0
        curSum = 0
        for i in range(1, n + 1):
            if curSum + i <= maxSum and i not in b:
                curSum += i
                cnt += 1
        return cnt
