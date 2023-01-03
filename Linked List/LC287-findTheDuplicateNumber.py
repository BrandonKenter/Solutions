'''
Slow and Fast Pointers - O(N) time / O(1) space
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow


'''
Hash Map - O(N) time / O(N) space
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis = set()

        for num in nums:
            if num in vis:
                return num
            vis.add(num)


'''
Sorting - O(Nlog(N)) time / O(N) space
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]