'''
Output Array
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output

'''
Prefix, Suffix and Output Arrays
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        out = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            left[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = postfix
            postfix *= nums[i]
        
        for i in range(len(nums)):
            out[i] = left[i] * right[i]
        return out