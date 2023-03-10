class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        maxi, maxi_arr = 0, []
        left_zeros, right_ones = 0, counts[1]

        for i in range(n + 1):
            s = left_zeros + right_ones
            if s == maxi:
                maxi_arr.append(i)
            elif s > maxi:
                maxi, maxi_arr = s, [i]
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                if nums[i] == 1:
                    right_ones -= 1
        return maxi_arr
