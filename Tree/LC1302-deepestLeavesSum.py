'''
DFS
'''
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = 0
        level_sum = 0

        def dfs(cur, depth):
            nonlocal deepest, level_sum
            if cur is None:
                return
            
            depth += 1
            if depth > deepest:
                deepest, level_sum = depth, cur.val
            elif depth == deepest:
                level_sum += cur.val
            
            dfs(cur.left, depth)
            dfs(cur.right, depth)
        dfs(root, 0)
        return level_sum

'''
BFS
'''
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            level_sum = 0
            for i in range(len(q)):
                cur = q.popleft()
                level_sum += cur.val

                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            
            if not q: return level_sum