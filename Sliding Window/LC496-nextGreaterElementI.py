class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {}
        for i, num in enumerate(nums1):
            nums1_map[num] = i

        res = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                if stack[-1] in nums1_map:
                    idx = nums1_map[stack[-1]]
                    res[idx] = num
                stack.pop()
            stack.append(num)
        return res