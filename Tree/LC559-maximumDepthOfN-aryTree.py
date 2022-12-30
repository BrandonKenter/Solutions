'''
DFS
'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0

        def dfs(cur, cur_depth):
            nonlocal max_depth
            if cur is None: return
            
            cur_depth += 1
            max_depth = max(max_depth, cur_depth)

            for nei in cur.children:
                dfs(nei, cur_depth)
        dfs(root, 0)
        return max_depth
        
'''
BFS
'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        levels = 0
        q = deque([root])
        while q:
            levels += 1
            for i in range(len(q)):
                cur = q.popleft()
                for child in cur.children:
                    q.append(child)
        return levels