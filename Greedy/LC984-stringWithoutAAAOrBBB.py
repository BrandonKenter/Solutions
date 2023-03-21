class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        a_count = b_count = 0
        res = []
        while a > 0 and b > 0:
            if a > b:
                if a_count <= 1:
                    res.append('a')
                    a_count += 1
                    a -= 1
                else:
                    res.append('b')
                    a_count = 0
                    b_count = 1
                    b -= 1
            else:
                if b_count <= 1:
                    res.append('b')
                    b_count += 1
                    b -= 1
                else:
                    res.append('a')
                    b_count = 0
                    a_count = 1
                    a -= 1
        if a: res.append('a' * a)
        if b: res.append('b' * b)
        return "".join(res)
