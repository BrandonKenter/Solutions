class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        dist_1, dist_2 = set(), set()
        
        for num in nums1:
            if num not in nums2_set:
                dist_1.add(num)
        for num in nums2:
            if num not in nums1_set:
                dist_2.add(num)
        
        return [list(dist_1), list(dist_2)]