'''
BFS
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        res = []
        level = 0

        while q:
            level_q = deque()
            for i in range(len(q)):
                cur = q.popleft()
                if level % 2:
                    level_q.appendleft(cur.val)
                else:
                    level_q.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            level += 1
            res.append(level_q)
        return res

'''
DFS
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        def dfs(cur, level):
            if cur is None:
                return
            
            if len(res) == level:
                q = deque([cur.val])
                res.append(q)
            elif level % 2 == 0:
                res[level].append(cur.val)
            else:
                res[level].appendleft(cur.val)
            
            level += 1
            dfs(cur.left, level)
            dfs(cur.right, level)
        
        res = []
        dfs(root, 0)
        return res