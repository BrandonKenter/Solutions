class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_seen = defaultdict(int) # tuples of each row seen

        # Get rows
        for r in range(len(grid)):
            row = []
            for c in range(len(grid[0])):
                row.append(grid[r][c])
            row = tuple(row)
            row_seen[row] += 1
        
        # Match cols
        count = 0
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            col = tuple(col)
            count += row_seen[col]
        return count