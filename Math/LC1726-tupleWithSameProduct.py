class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts, res, n = defaultdict(int), 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                res += 8 * counts[nums[i] * nums[j]]
                counts[nums[i] * nums[j]] += 1
        return res
        