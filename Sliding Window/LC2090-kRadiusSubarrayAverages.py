class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        left = 0
        cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]
            if right - left + 1 == k * 2 + 1:
                res[right-k] = cur_sum // (right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return res
