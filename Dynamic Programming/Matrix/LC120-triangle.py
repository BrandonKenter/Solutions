'''
Memoization
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for col in range(n)] for row in range(n)]

        def helper(i, j):
            if i == n-1: return triangle[i][j]
            if dp[i][j] != -1: return dp[i][j]

            down = helper(i+1, j)
            down_right = helper(i+1, j+1)
            dp[i][j] = triangle[i][j] + min(down, down_right)
            return dp[i][j]
        return helper(0, 0)


'''
Tabulation
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for col in range(n)] for row in range(n)]

        for j in range(n): dp[n-1][j] = triangle[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(i+1):
                down = dp[i+1][j]
                down_right = dp[i+1][j+1]
                dp[i][j] = triangle[i][j] + min(down, down_right)
        return dp[0][0]