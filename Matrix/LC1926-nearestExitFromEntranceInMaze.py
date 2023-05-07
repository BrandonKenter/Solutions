class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        vis = set([(entrance[0], entrance[1])])
        q = deque([(entrance[0], entrance[1])])
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r in [0, m - 1] or c in [0, n - 1]) and maze[r][c] == '.' and [r, c] != entrance:
                    return dist
                
                for dr, dc in directions:
                    nei_r, nei_c = dr + r, dc + c
                    if (
                        nei_r in range(m) and
                        nei_c in range(n) and 
                        (nei_r, nei_c) not in vis and 
                        maze[nei_r][nei_c] == '.'
                    ):
                        q.append((nei_r, nei_c))
                        vis.add((nei_r, nei_c))
            dist += 1
        return -1