class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(list(str(num)))
        num1, num2 = [num[0], num[2]], [num[1], num[3]]
        num1, num2 = int("".join(num1)), int("".join(num2))
        return num1 + num2