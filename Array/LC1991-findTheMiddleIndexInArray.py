class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        leftmost = -1
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                if leftmost == -1:
                    leftmost = i
            leftSum += nums[i]
        return leftmost
        