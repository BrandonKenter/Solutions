class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            prev = res[-1]
            new = [1] * (len(prev) + 1)
            for j in range(1, len(new) - 1):
                new[j] = prev[j - 1] + prev[j]
            res.append(new)
        return res
    