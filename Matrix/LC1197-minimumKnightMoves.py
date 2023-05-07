class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        q = deque([(0, 0)])
        vis = set([(0, 0)])
        moves = 0

        while q:
            for i in range(len(q)):
                cur_x, cur_y = q.popleft()
                if cur_x == x and cur_y == y:
                    return moves
                
                for dx, dy in directions:
                    nei_x, nei_y = dx + cur_x, dy + cur_y
                    if (nei_x, nei_y) not in vis:
                        q.append((nei_x, nei_y))
                        vis.add((nei_x, nei_y))
            moves += 1