class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = [n for n in num]
        changed = False
        for i in range(len(num)):
            if change[(int(num[i]))] > int(num[i]):
                num[i] = str(change[(int(num[i]))])
                changed = True
            elif changed and change[(int(num[i]))] == int(num[i]):
                num[i] = str(change[(int(num[i]))])
            else:
                if changed:
                    return "".join(num)
        return "".join(num)
            