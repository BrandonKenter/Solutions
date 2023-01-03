class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M - 1
        t, b = 0, N - 1
        
        while l <= r:
            for i in range(r - l):
                # Save top_l
                top_l = matrix[t][l + i]
                
                # bot_l -> top_l
                matrix[t][l + i] = matrix[b - i][l]
                
                # bot_r -> bot_l
                matrix[b - i][l] = matrix[b][r - i]
                
                # top_r -> bot_l
                matrix[b][r - i] = matrix[t + i][r]
                
                # top_l -> top_r
                matrix[t + i][r] = top_l
            l += 1
            r -= 1
            t += 1
            b -= 1
