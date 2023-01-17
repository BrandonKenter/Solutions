'''
Double for loop
O(N^2) time / O(1) space
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count


'''
Hash map
O(N) time / O(N) space
'''
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        for num in nums:
            count += seen[num-k] + seen[num+k]
            seen[num] += 1
        return count