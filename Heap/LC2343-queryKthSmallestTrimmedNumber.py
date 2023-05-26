class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            k, trim = query
            max_h = []
            for i, num in enumerate(nums):
                trimmed_num = int(num[-trim:])
                heappush(max_h, (-1 * trimmed_num, -1 * i))
                if len(max_h) > k:
                    heappop(max_h)
            _, smallest_i = heappop(max_h)
            res.append(-1 * smallest_i)
        return res
                