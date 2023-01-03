'''
Hash Set - O(N) time / O(N) space
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for n in nums:
            if n - 1 in nums_set:
                continue
            length = 0
            while n + length in nums_set:
                length += 1
            max_len = max(max_len, length)
        return max_len

'''
Sorting - O(Nlog(N)) time / O(1) space
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        max_len = 1
        cur_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    cur_len += 1
                else:
                    max_len = max(max_len, cur_len)
                    cur_len = 1
        return max(max_len, cur_len)