class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for _ in range(1, n):
            i = 0
            new = []
            while i < len(num):
                j = i
                while j < len(num) and num[i] == num[j]:
                    j += 1
                length = j - i
                new.append(str(length) + str(num[i]))
                i = j
            num = "".join(new)
        return num
