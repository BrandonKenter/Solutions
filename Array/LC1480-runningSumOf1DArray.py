class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = nums
        for i in range(1, len(nums)):
            res[i] += res[i-1]
        return res
        