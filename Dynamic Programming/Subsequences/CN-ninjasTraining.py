'''
Memoization
'''
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for col in range(4)] for row in range(n)]
    
    def helper(day, last):
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi
        if dp[day][last] != -1: return dp[day][last]
        
        maxi = 0
        for i in range(3):
            p = 0
            if i != last:
                p = points[day][i] + helper(day-1, i)
            maxi = max(maxi, p)
        dp[day][last] = maxi
        return dp[day][last]
    return helper(n-1, 3)


'''
Tabulation
'''
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for col in range(4)] for row in range(n)]
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    
    for day in range(1, n):
        for last in range(4):
            maxi = 0
            for i in range(3):
                p = 0
                if i != last:
                    p = points[day][i] + dp[day-1][i]
                maxi = max(maxi, p)
            dp[day][last] = maxi
    return dp[n-1][3]