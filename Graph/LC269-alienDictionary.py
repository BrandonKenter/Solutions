'''
DFS
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for w1, w2 in zip(words[:-1], words[1:]):
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for i in range(min_len):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    adj[c1].add(c2)
                    break
        
        vis = set()
        path_vis = set()
        def dfs(cur):
            if cur in path_vis:
                return False
            if cur in vis:
                return True
            
            path_vis.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            path_vis.remove(cur)
            vis.add(cur)
            res.append(cur)
            return True

        res = []
        for c in adj.keys():
            if not dfs(c):
                return ""
        return "".join(res[::-1])


'''
BFS (Kahn's)
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        indegree = {c:0 for word in words for c in word}
        for w1, w2 in zip(words[:-1], words[1:]):
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for i in range(min_len):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(res) if len(res) == len(adj) else ""
