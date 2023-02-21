'''
Tabulation
1D - O(N) space
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n, maxi, last_i = len(nums), 1, 0
        dp = [1] * n
        par = [i for i in range(n)]

        for i in range(n):
            for prev in range(i):
                if nums[i] % nums[prev] == 0 and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    par[i] = prev
            if dp[i] > maxi:
                maxi = dp[i]
                last_i = i

        lds = [nums[last_i]]
        while par[last_i] != last_i:
            last_i = par[last_i]
            lds.append(nums[last_i])
        return lds