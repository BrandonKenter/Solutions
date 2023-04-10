class Solution:
    def halveArray(self, nums: List[int]) -> int:
        max_h = [-num for num in nums]
        heapify(max_h)
        start_s = s = sum(nums)
        ops = 0
        while s > start_s / 2:
            maxi = heappop(max_h)
            new = maxi / 2
            s += new
            ops += 1
            heappush(max_h, new)
        return ops
