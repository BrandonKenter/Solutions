class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        i = 0
        while x ** i <= bound:
            j = 0
            while x ** i + y ** j <= bound:
                res.add(x ** i + y ** j)
                j += 1
                if y == 1:
                    break
            i += 1
            if x == 1:
                break
        return list(res)
        