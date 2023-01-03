class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cols = defaultdict(int)
        cols[0] = 0
        n = len(wall)
        
        for row in wall:
            col = 0
            for i in range(len(row) - 1):
                col += row[i]
                cols[col] += 1
        return n - max(cols.values())