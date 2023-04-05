class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        x, a = 0, []
        for i in word:
            x = x * 10 + int(i)
            if x % m == 0:
                a+=[1]
            else:
                a += [0]
            x %= m
        return a
    