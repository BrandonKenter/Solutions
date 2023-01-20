class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N' : (0, 1), 'S' : (0, -1), 'E' : (1, 0), 'W' : (-1, 0)}
        vis = set([(0, 0)])
        x = y = 0
        for dir in path:
            x += directions[dir][0]
            y += directions[dir][1]
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False