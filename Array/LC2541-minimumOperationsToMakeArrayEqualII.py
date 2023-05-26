class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return -1 if nums1 != nums2 else 0

        increase = 0
        decrease = 0
        for num1, num2 in zip(nums1, nums2):
            if num1 == num2:
                continue
            elif num2 > num1:
                if (num2 - num1) % k:
                    return -1
                increase += num2 - num1
            else:
                if (num1 - num2) % k:
                    return -1
                decrease += num1 - num2
        
        if increase == decrease:
            return increase // k
        else:
            return -1 
            