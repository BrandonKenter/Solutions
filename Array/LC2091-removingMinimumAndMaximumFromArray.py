class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums) - 1
        min_i, max_i = nums.index(min(nums)), nums.index(max(nums))

        if min_i == max_i:
            return min(min_i + 1, max_i + 1, n - min_i + 1, n - max_i + 1)
        # max is first from left
        left_max = max_i + 1 + abs(min_i - max_i)
        # min is first from left
        left_min = min_i + 1 + abs(max_i - min_i)
        # max is first from right
        right_max = n - max_i + 1 + abs(max_i - min_i)
        # min is first from right
        right_min = n - min_i + 1 + abs(min_i - max_i)
        # min from left, max from right
        mid_min_left = min_i + 1 + n - max_i + 1
        # max from left, min from right
        mid_min_right = n - min_i + 1 + max_i + 1
        return min(left_max, left_min, right_max, right_min, mid_min_left, mid_min_right)
        