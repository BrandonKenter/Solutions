'''
Sliding Window
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.subs(nums, k) - self.subs(nums, k - 1)

    def subs(self, nums, goal):
        s = left = res = 0
        for right in range(len(nums)):
            s += nums[right] % 2
            while left <= right and s > goal:
                s -= nums[left] % 2
                left += 1
            res += right - left + 1
        return res

'''
Prefix Sums
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = defaultdict(int)
        pre[0] = 1
        count = 0
        res = left = 0
        for right in range(len(nums)):
            if nums[right] % 2: 
                count += 1
            res += pre[count-k]
            pre[count] += 1
        return res