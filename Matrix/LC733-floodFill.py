'''
DFS
O(M*N) time / O(M*N) space
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        s_color = image[sr][sc]
        vis = set()

        def dfs(r, c):
            vis.add((r, c))
            image[r][c] = color
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and 
                    image[nei_r][nei_c] == s_color
                ):
                    dfs(nei_r, nei_c)
        
        dfs(sr, sc)
        return image



'''
BFS
O(M*N) time / O(M*N) space
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        s_color = image[sr][sc]
        vis = set([(sr, sc)])
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n) and 
                    (nei_r, nei_c) not in vis and
                    image[nei_r][nei_c] == s_color
                ):
                    vis.add((nei_r, nei_c))
                    q.append((nei_r, nei_c))
                    image[nei_r][nei_c] = color

        return image
