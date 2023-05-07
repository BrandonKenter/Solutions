class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        q = deque([(start[0], start[1])])
        vis = set([(start[0], start[1])])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def get_wall_coords(r, c, direction):
            dr, dc = direction
            while r + dr in range(m) and c + dc in range(n) and maze[r + dr][c + dc] != 1:
                r, c = r + dr, c + dc
            return [r, c]

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if [r, c] == destination:
                    return True
                
                for direction in directions:
                    next_r, next_c = get_wall_coords(r, c, direction)
                    if (next_r, next_c) not in vis:
                        q.append((next_r, next_c))
                        vis.add((next_r, next_c))
        return False
