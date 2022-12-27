'''
DFS
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for word_a, word_b in zip(words[:-1], words[1:]):
            min_len = min(len(word_a), len(word_b))
            if len(word_a) > len(word_b) and word_a[:min_len] == word_b[:min_len]:
                return ""
            for i in range(min_len):
                char_a, char_b = word_a[i], word_b[i]
                if char_a != char_b:
                    adj[char_a].add(char_b)
                    break
            
        vis = set()
        cur_vis = set()

        def dfs(cur):
            if cur in vis:
                return True
            if cur in cur_vis:
                return False
            
            cur_vis.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            cur_vis.remove(cur)
            vis.add(cur)
            ans.append(cur)
            return True

        ans = []
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(ans[::-1])


'''
BFS (Kahn's)
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        indegree = {c : 0 for w in words for c in w}

        for word_a, word_b in zip(words[:-1], words[1:]):
            min_len = min(len(word_a), len(word_b))
            if len(word_a) > len(word_b) and word_a[:min_len] == word_b[:min_len]:
                return ""
            for i in range(min_len):
                char_a, char_b = word_a[i], word_b[i]
                if char_a != char_b:
                    if char_b not in adj[char_a]:
                        adj[char_a].add(char_b)
                        indegree[char_b] += 1
                    break
        
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        ans = []
        while q:
            c = q.popleft()
            ans.append(c)

            for nei_c in adj[c]:
                indegree[nei_c] -= 1
                if indegree[nei_c] == 0:
                    q.append(nei_c)
        
        if len(ans) != len(adj):
            return ""
        return "".join(ans)