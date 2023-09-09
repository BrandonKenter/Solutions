class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {} # digit sum : [indices with this digit sum]
        maxi = -1
        for number in nums:
            num = number
            digit_sum = 0
            while num != 0:
                digit = num % 10
                digit_sum += digit
                num //= 10
            if digit_sum in digit_sums:
                if number > digit_sums[digit_sum]:
                    maxi = max(maxi, digit_sums[digit_sum] + number)
                    digit_sums[digit_sum] = number 
                else:
                    maxi = max(maxi, digit_sums[digit_sum] + number)
            else:
                digit_sums[digit_sum] = number 
        return maxi
        