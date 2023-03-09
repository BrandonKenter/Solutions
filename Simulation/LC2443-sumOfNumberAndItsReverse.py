class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            j = int(str(i)[::-1])
            if i + j == num: 
                return True
        return False
        