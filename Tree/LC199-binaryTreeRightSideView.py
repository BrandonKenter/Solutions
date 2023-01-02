'''
DFS
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(cur, level):
            if cur is None:
                return
            
            if level == len(ans):
                ans.append(cur.val)

            dfs(cur.right, level + 1)
            dfs(cur.left, level + 1)
        dfs(root, 0)
        return ans

'''
BFS
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        ans = []
        q = deque([root])

        while q:
            ans.append(q[-1].val)
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return ans