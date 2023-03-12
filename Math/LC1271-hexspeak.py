class Solution:
    def toHexspeak(self, num: str) -> str:
        letters = {'A', 'B', 'C', 'D', 'E', 'F'}
        num = hex(int(num))[2:]
        res = []
        for c in num:
            if c.isnumeric():
                if c != '0' and c != '1':
                    return "ERROR"
                elif c == '0':
                    res.append('O')
                else:
                    res.append('I')
            else:
                if c.upper() not in letters:
                    return "ERROR"
                else:
                    res.append(c.upper())
        return "".join(res)
