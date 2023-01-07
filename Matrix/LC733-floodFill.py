class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        v = set()
        old = image[sr][sc]
        
        def dfs(r, c):
            if (
                r not in range(M) or 
                c not in range(N) or 
                (r, c) in v or 
                image[r][c] != old
            ):
                return
            
            v.add((r, c))
            image[r][c] = color
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = dr + r, dc + c
                dfs(row, col)
        dfs(sr, sc)
        return image