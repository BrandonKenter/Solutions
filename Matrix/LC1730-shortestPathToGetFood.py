class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        vis = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    vis.add((r, c))
                    q.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        level = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == '#':
                    return level

                for dr, dc in directions:
                    nei_r, nei_c = dr + r, dc + c
                    if (
                        nei_r in range(m) and 
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        grid[nei_r][nei_c] in 'O#'
                    ):
                        vis.add((nei_r, nei_c))
                        q.append((nei_r, nei_c))
            level += 1
        return -1
        