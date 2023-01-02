class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parents = [i for i in range(n * n)]
        sizes = [1] * (n * n)

        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(x, y):
            x_par, y_par = find(x), find(y)

            if x_par == y_par:
                return
            
            if sizes[x_par] < sizes[y_par]:
                sizes[y_par] += sizes[x_par]
                parents[x_par] = y_par
            else:
                sizes[x_par] += sizes[y_par]
                parents[y_par] = x_par

        def isValid(r, c):
            if r >= 0 and r <= n - 1 and c >= 0 and c <= n - 1 and grid[r][c] == 1:
                return True
            else:
                return False

        # step 1: run union-find on the grid to connect the components
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0: continue
                i = (r * n + c) # index of current cell
                
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if isValid(nei_r, nei_c):
                        j = (nei_r * n + nei_c) # index of neighbor cell
                        if find(i) != find(j):
                            union(i, j)
        
        # step 2: find the cell that maximizes the size of an island
        max_size = max(1, sizes[0]) # could have a cell of only 1's
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1: continue
                cur_size = 0 
                v = set() # visited ultimate parents
                i = (r * n + c)
            
                for dr, dc in directions:
                    nei_r, nei_c = r + dr, c + dc
                    if isValid(nei_r, nei_c):
                        j = (nei_r * n + nei_c)
                        nei_up = find(j) # ultimate parent of neighbor cell
                        if nei_up not in v: 
                            v.add(nei_up)
                            nei_size = sizes[nei_up]
                            cur_size += nei_size
                max_size = max(max_size, 1 + cur_size)
        return max_size