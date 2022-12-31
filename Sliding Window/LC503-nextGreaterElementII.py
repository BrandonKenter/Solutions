class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums * 2
        res = [-1] * len(nums)
        stack = []
        
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                stack_i, stack_num = stack.pop()
                res[stack_i] = num
            stack.append((i, num))
        return res[:n]