class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_r = 0
        max_c = 0
        for i in range(len(stones)):
            max_r = max(max_r, stones[i][0])
            max_c = max(max_c, stones[i][1])

        parents = [i for i in range(max_r + max_c + 2)]
        sizes = [1] * (max_r + max_c + 2)

        def find(i):
            print(i)
            if i == parents[i]:
                return i
            parents[i] = find(parents[i])
            return parents[i]
        
        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return
            
            if sizes[p1] < sizes[p2]:
                sizes[p2] += sizes[p1]
                parents[p1] = p2
            else:
                sizes[p1] += sizes[p2]
                parents[p2] = p1
        
        stone_nodes = {}
        for i in range(len(stones)):
            r = stones[i][0]
            c = stones[i][1] + max_r + 1
            union(r, c)
            stone_nodes[r] = 1
            stone_nodes[c] = 1

        cnt = 0
        for i, v in stone_nodes.items():
            if find(i) == i:
                cnt += 1
        return len(stones) - cnt