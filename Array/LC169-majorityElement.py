'''
Update Frequency - O(N) time / O(1) space
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        max_ele = nums[0]

        for num in nums:
            if count == 0:
                max_ele = num
            if num == max_ele: 
                count += 1
            else:
                count -= 1
        return max_ele

'''
Hash Map - O(N) time / O(N) space
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)
    