class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        dist_1, dist_2 = [], []
        
        for num in nums1_set:
            if num not in nums2_set:
                dist_1.append(num)
        for num in nums2_set:
            if num not in nums1_set:
                dist_2.append(num)
        
        return [dist_1, dist_2]
