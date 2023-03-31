class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right, top, bot = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bot:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1

            if left > right or top > bot:
                break

            for i in range(right, left - 1, -1):
                res.append(matrix[bot][i])
            bot -= 1

            for i in range(bot, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
