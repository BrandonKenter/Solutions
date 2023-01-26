class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        indices = [i for i in range(n)]
        for direction, amount in shift:
            if direction == 0:
                for i in range(n):
                    indices[i] -= amount
                    indices[i] += n
                    indices[i] %= n
            else:
                for i in range(n):
                    indices[i] += amount
                    indices[i] %= n

        res = ["" for i in range(n)]
        for i in range(n):
            index = indices[i]
            res[index] = s[i]
        return "".join(res)