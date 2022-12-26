class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        a, b = list(a), list(b)
        carry = 0
        while a or b or carry:
            a_val = int(a.pop()) if a else 0
            b_val = int(b.pop()) if b else 0
            new_val = carry + a_val + b_val
            carry = new_val // 2
            new_val = new_val % 2
            res.append(str(new_val))
        return "".join(res)[::-1]
