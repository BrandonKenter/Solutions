class Solution:
    def findScore(self, nums: List[int]) -> int:
        vis = set()
        min_h = []

        for i, num in enumerate(nums):
            heappush(min_h, (num, i))
        
        res = 0
        while len(vis) < len(nums):
            cur_num, cur_i = heappop(min_h)
            if cur_i not in vis:
                vis.add(cur_i)
                res += cur_num
                if cur_i > 0: vis.add(cur_i - 1)
                if cur_i < len(nums) - 1: vis.add(cur_i + 1)
        return res
