class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_sums = []
        for i in range(len(nums)):
            sub_sum = 0
            for j in range(i, len(nums)):
                sub_sum += nums[j]
                sub_sums.append(sub_sum)
        sub_sums.sort()
        return sum(sub_sums[left-1:right]) % (10**9+7)
        