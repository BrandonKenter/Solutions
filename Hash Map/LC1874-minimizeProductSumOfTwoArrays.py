'''
O(Nlog(N)) time / O(1) space
'''
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        prod_sum = 0
        for i in range(len(nums1)):
            prod = nums1[i] * nums2[len(nums2) - 1 - i]
            prod_sum += prod
        return prod_sum


'''
O(N) time / O(N) space
'''
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        freq1 = [0] * 101
        freq2 = [0] * 101
        for num in nums1: freq1[num] += 1
        for num in nums2: freq2[num] += 1

        prod_sum = 0
        i, j = 0, len(freq2) - 1
        while i < len(freq1) and j >= 0:
            if freq1[i] == 0:
                i += 1
            elif freq2[j] == 0:
                j -= 1
            else:
                prod_sum += i * j
                freq1[i] -= 1
                freq2[j] -= 1
        return prod_sum