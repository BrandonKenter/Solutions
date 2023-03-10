'''
Memoization
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0 for z in range(n)] for y in range(n)] for x in range(m)]

        def helper(i, j1, j2):
            if j1 < 0 or j2 < 0 or j1 > n-1 or j2 > n-1: return float('-inf')
            if i == m-1: 
                if j1 == j2: return grid[i][j1]
                else: return grid[i][j1] + grid[i][j2]
            if dp[i][j1][j2] != -1: return dp[i][j1][j2]
            
            maxi = float('-inf')
            for jd1 in range(-1, 2):
                for jd2 in range(-1, 2):
                    value = 0
                    if j1 == j2: value = grid[i][j1]
                    else: value = grid[i][j1] + grid[i][j2]
                    value += helper(i+1, j1+jd1, j2+jd2)
                    maxi = max(maxi, value)
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]
        return helper(0, 0, n-1)


'''
Tabulation
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1 for z in range(n)] for y in range(n)] for x in range(m)]

        for j1 in range(n):
            for j2 in range(n):
                if j1 == j2: dp[m-1][j1][j2] = grid[m-1][j1]
                else: dp[m-1][j1][j2] = grid[m-1][j1] + grid[m-1][j2]
        
        for i in range(m-2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    maxi = float('-inf')
                    for jd1 in range(-1, 2):
                        for jd2 in range(-1, 2):
                            value = 0
                            if j1 == j2: value = grid[i][j1]
                            else: value = grid[i][j1] + grid[i][j2]
                            if j1+jd1 >= 0 and j1+jd1 < n and j2+jd2 >= 0 and j2+jd2 < n:
                                value += dp[i+1][j1+jd1][j2+jd2]
                            else: value += float('-inf')
                            maxi = max(maxi, value)
                    dp[i][j1][j2] = maxi
        return dp[0][0][n-1]
