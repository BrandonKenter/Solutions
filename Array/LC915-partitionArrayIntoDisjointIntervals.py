class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        post = [0] * len(nums) # postfix minimums (exclusive)

        post_mini = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            post[i] = post_mini
            post_mini = min(post_mini, nums[i])
        
        maxi = nums[0]
        for i in range(len(nums)):
            maxi = max(maxi, nums[i])
            if maxi <= post[i]:
                return i + 1
