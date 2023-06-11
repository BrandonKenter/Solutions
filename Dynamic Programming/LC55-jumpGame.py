'''
Top-down
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None for i in range(len(nums))]
        nums.reverse()

        def helper(i):
            if i <= 0:
                return True
            if dp[i] != None:
                return dp[i]

            reached = False
            for j in range(nums[i], 0, -1):
                choice = helper(i-j)
                if choice: 
                    reached = True
                    break
            dp[i] = reached
            return dp[i]
        
        return helper(len(nums) - 1)


'''
Bottom-up
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]
        dp[0] = True
        
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] >= i-j and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
        