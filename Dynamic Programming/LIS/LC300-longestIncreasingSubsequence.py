'''
Memoization
Not recommended to learn
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for col in range(n+1)] for row in range(n)]

        def helper(i, prev_i):
            if i == n: return 0
            if dp[i][prev_i+1] != -1: return dp[i][prev_i+1]
            
            take = 1 + helper(i+1, i) if prev_i == -1 or nums[i] > nums[prev_i] else 0
            not_take = 0 + helper(i+1, prev_i)
            dp[i][prev_i+1] = max(take, not_take)
            return dp[i][prev_i+1]
        return helper(0, -1)


'''
Tabulation
2D - O(N*N) space
Not recommended to learn
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for prev_i in range(n+1)] for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for prev_i in range(i-1, -2, -1):
                take = 1 + dp[i+1][i+1] if prev_i == -1 or nums[i] > nums[prev_i] else 0
                not_take = 0 + dp[i+1][prev_i+1]
                dp[i][prev_i+1] = max(take, not_take)
        return dp[0][-1+1]


'''
Tabulation
1D - O(N) space
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxi = 1

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[prev])
            maxi = max(maxi, dp[i])
        return maxi


'''
Tabulation
1D - O(N) space
Include par array to recover LIS
This version is for when we are asked to print a LIS
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        par = [i for i in range(n)]
        maxi = 1
        last_i = 0

        for i in range(n):
            for prev in range(i):
                if nums[prev] < nums[i] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    par[i] = prev
            if dp[i] > maxi:
                maxi = dp[i]
                last_i = i

        lis = [nums[last_i]]
        while par[last_i] != last_i:
            last_i = par[last_i]
            lis.append(nums[last_i])
        return lis[::-1]
