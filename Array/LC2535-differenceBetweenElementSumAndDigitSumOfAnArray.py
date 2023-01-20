class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            while num:
                digit = num % 10
                digit_sum += digit
                num = num // 10
        return abs(element_sum - digit_sum)