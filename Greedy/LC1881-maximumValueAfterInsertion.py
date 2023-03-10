class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if int(n) > 0:
            i = 0
            while i < len(n):
                if n[i] < str(x):
                    return n[:i] + str(x) + n[i:]
                i += 1
            return n + str(x)
        else:
            i = 1
            while i < len(n):
                if n[i] > str(x):
                    return n[:i] + str(x) + n[i:]
                i += 1
            return n + str(x)
