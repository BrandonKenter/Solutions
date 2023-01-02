class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            new_digit = digit + carry
            carry = new_digit // 10
            new_digit = new_digit % 10
            res.append(new_digit)
        if carry:
            res.append(carry)
        return res[::-1]