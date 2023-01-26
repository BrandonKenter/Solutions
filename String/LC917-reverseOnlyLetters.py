class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = [None for i in range(len(s))]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left].isalpha() == False:
                res[left] = s[left]
                left += 1
            elif s[right].isalpha() == False:
                res[right] = s[right]
                right -= 1
            else:
                res[left], res[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(res)