class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {}
        for i, num in enumerate(nums2):
            nums2_map[num] = i
        
        nums1_map = {}
        for i, num in enumerate(nums1):
            nums1_map[i] = nums2_map[num]
        
        return nums1_map.values()