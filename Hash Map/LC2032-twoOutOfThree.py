class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1_set, n2_set, n3_set = set(nums1), set(nums2), set(nums3)
        res = set()
        for num in nums1:
            if num in n2_set or num in n3_set:
                res.add(num)
        for num in n2_set:
            if num in n1_set or num in n3_set:
                res.add(num)
        return list(res)