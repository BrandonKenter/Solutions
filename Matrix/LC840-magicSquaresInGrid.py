class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        # Iterate through every top-left cell in the 3x3 grid
        for i in range(m-3+1):
            for j in range(n-3+1):
                count += self.is_magic(grid, i, j)
        return count

    # Use a helper method
    # Allows us to return early if a condition is not met
    # Also cleans up the code a bit
    def is_magic(self, grid, i, j):
        distinct = set() # Supposed to hold numbers 1 -> 9 at end of traversal of 3x3 grid
        row_sums = defaultdict(int) 
        col_sums = defaultdict(int)
        neg_diag_sum = 0 
        pos_diag_sum = 0

        # Iterate through the 3x3 grid
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                if grid[r][c] == 0 or grid[r][c] >= 10:
                    return 0
                distinct.add(grid[r][c])
                row_sums[r] += grid[r][c]
                col_sums[c] += grid[r][c]
                # Diagonals must subtract by i and j because of offset
                # Negative diagonal 
                if r - i == c - j :
                    neg_diag_sum += grid[r][c]
                # Positive diagonal
                if r - i + c - j == 2:
                    pos_diag_sum += grid[r][c]
        
        # Check if all row and column cells are the same
        prev_row_sum = row_sums[i]
        prev_col_sum = col_sums[j]
        for cur_row_sum in row_sums.values():
            if cur_row_sum != prev_row_sum:
                break
        else:
            for cur_col_sum in col_sums.values():
                if cur_col_sum != prev_col_sum:
                    break
            else:
                if prev_row_sum == prev_col_sum == neg_diag_sum == pos_diag_sum and len(distinct) == 9:
                    return 1
        return 0
        