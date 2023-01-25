class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        n, i, res = len(number), 0, []
        while i < n:
            if n - 1 - i + 1 > 4:
                res.append(number[i:i+3] + '-')
                i += 3
            elif n - 1 - i + 1 == 4:
                res.append(number[i:i+2] + '-' + number[i+2:i+4])
                i += 4
            elif n - 1 - i + 1 == 3:
                res.append(number[i:i+3])
                i += 3
            elif n - 1 - i + 1 == 2:
                res.append(number[i:i+2])
                i += 2
        return "".join(res)