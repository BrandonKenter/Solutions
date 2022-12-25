class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        count = 0
        s = 0
        for num in nums:
            s += num
            count += prefix_sums[s - k]
            prefix_sums[s] += 1
        return count