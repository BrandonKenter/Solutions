class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parents = [i for i in range(m * n)]
        sizes = [1] * (m * n)

        def find(i):
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py: return False

            if sizes[px] < sizes[py]:
                sizes[py] += sizes[px]
                parents[px] = py
            else:
                sizes[px] += sizes[py]
                parents[py] = px
            return True

        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = []
        vis = set()
        islands = 0
        for r, c in positions:
            if (r, c) in vis:
                ans.append(islands)
                continue
            
            vis.add((r, c))
            islands += 1
            for dr, dc in directions:
                nei_r, nei_c = dr + r, dc + c
                if (
                    nei_r in range(m) and 
                    nei_c in range(n)
                ):
                    i = r * n + c
                    j = nei_r * n + nei_c
                    if (nei_r, nei_c) in vis and find(i) != find(j):
                        union(i, j)
                        islands -= 1
            ans.append(islands)
        return ans