class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = j = -1
        for k in range(len(num) - 1, -1, -1):
            if int(num[k]) % 2:
                i = 0
                j = k
                break
        return num[i:j+1]