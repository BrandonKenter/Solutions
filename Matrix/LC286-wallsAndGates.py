class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        M, N = len(rooms), len(rooms[0])
        v = set()
        q = deque()
        for r in range(M):
            for c in range(N):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    v.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (
                        row not in range(M) or 
                        col not in range(N) or 
                        (row, col) in v or
                        rooms[row][col] != 2147483647
                    ):
                        continue
                    
                    q.append((row, col))
                    v.add((row, col))
            dist += 1
        