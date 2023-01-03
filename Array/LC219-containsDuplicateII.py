'''
Hash Map - O(N) time / O(N) space
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vis = {}
        for i, num in enumerate(nums):
            if num in vis and i - vis[num] <= k:
                return True
            vis[num] = i
        return False


'''
Double For Loop - O(N^2) time / O(1) space
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False