class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        cur = 0
        for bit in nums:
            cur <<= 1
            cur += bit
            res.append(cur % 5 == 0)
        return res
        