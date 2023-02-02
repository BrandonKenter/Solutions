class Solution:
    def alternateDigitSum(self, n: int) -> int:
        if n < 10: return n

        div = 10
        while div * 10 <= n:
            div *= 10
        
        dig_sum, digits, i = 0, n, 0
        while digits:
            digit = digits // div
            if i % 2 == 0:
                dig_sum += digit
            else:
                dig_sum -= digit
            digits -= digit * div
            div //= 10
            i += 1
        return dig_sum