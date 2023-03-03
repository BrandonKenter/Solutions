class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num, base = n, k
        remainder = num
        power = 0
        while base ** power <= num:
            power += 1
        power -= 1

        res = 0
        while remainder:
            res += (remainder//(base**power))
            remainder = remainder % (base**power)
            power -= 1
        return res
    