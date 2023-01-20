class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums), 2):
            freq, num = nums[i-1], nums[i]
            res.extend(freq * [num])
        return res