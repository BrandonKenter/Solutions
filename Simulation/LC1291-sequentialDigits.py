class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        l, r = len(str(low)), len(str(high))
        for i in range(l, r + 1):
            for j in range(0, 9-i+1):
                num = int(digits[j:j+i])
                if num >= low and num <= high:
                    res.append(num)
        return res
