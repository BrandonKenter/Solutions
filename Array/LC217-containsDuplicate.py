'''
Hash Map - O(N) time / O(N) space
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        v = set()
        for n in nums:
            if n in v:
                return True
            v.add(n)
        return False

'''
Double For Loop - O(N^2) time / O(1) space
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

'''
Sorting - O(Nlog(N)) time / O(1) space
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    