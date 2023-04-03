class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            s = 0
            for num in nums:
                s += math.ceil(num / mid)
            if s <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
        