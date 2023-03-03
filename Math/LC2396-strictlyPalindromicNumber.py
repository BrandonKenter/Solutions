class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            digits = self.get_base_digits(n, i)
            if not self.is_palindrome(digits):
                return False
        return True


    def get_base_digits(self, num, base):
        remainder = num
        power = 0
        while base ** power <= num:
            power += 1
        power -= 1

        res = []
        while remainder:
            res.append(remainder//(base**power))
            remainder = remainder % (base**power)
            power -= 1
        return res


    def is_palindrome(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
            