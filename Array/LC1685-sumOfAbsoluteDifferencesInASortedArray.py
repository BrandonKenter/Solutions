class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, r = len(nums), sum(nums)
        l = 0
        res = [0] * n
        for i, num in enumerate(nums):
            r -= num
            res[i] += r - (num * (n-i-1)) # right dif
            res[i] += (num * i) - l # left dif
            l += num
        return res
