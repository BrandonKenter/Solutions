'''
Sliding Window
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.subs(nums, goal) - self.subs(nums, goal - 1)

    def subs(self, nums, goal):
        s = left = res = 0
        for right in range(len(nums)):
            s += nums[right]
            while left <= right and s > goal:
                s -= nums[left]
                left += 1
            res += right - left + 1
        return res

'''
Prefix Sums
'''
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = defaultdict(int)
        pre[0] = 1
        s = left = res = 0
        for right in range(len(nums)):
            s += nums[right]
            res += pre[s - goal]
            pre[s] += 1
        return res