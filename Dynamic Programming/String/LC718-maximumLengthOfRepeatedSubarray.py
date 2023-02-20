'''
Memoization
Passes test cases but I have absolutely no idea how the no match logic works
I think we have the match/nomatch recursive calls outside the if/else condition so
    we don't overwrite dp[i][j]
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[-1 for j in range(n)] for i in range(m)]
        
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]         
            
            match = 1 + helper(i-1, j-1)
            nomatch = min(helper(i,j-1), helper(i-1, j), 0)
            if nums1[i] == nums2[j]:
                dp[i][j] = match
                return dp[i][j]
            else:
                dp[i][j] = nomatch
                return dp[i][j]
            
        helper(m-1, n-1)
        maxi = 0
        for i in range(m):
            for j in range(n):
                maxi = max(maxi, dp[i][j])
        return maxi

    
'''
Tabulation
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
                ans = max(ans, dp[i][j])
        return ans
