'''
Memoization
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def helper(i, k):
            if i == 0:
                if k - nums[i] == target and k + nums[i] == target:
                    return 2
                elif k - nums[i] == target or k + nums[i] == target:
                    return 1
                else:
                    return 0
            if (i, k) in dp:
                return dp[(i, k)]
            
            subtract = helper(i-1, k-nums[i])
            add = helper(i-1, k+nums[i])
            dp[(i, k)] = subtract + add
            return dp[(i, k)]
        return helper(n-1, 0)


'''
Tabulation
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        dp = [[0 for col in range(2 * total + 1)] for row in range(n)]

        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, n):
            for k in range(-total, total + 1):
                if dp[i-1][k+total] > 0:
                    dp[i][k + nums[i] + total] += dp[i - 1][k + total]
                    dp[i][k - nums[i] + total] += dp[i - 1][k + total]

        return 0 if abs(target) > total else dp[n-1][target + total]


