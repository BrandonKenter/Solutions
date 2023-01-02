class Solution:
    def topView(self, root):
        if not root: return
        col_to_topnode = {}
        q = deque() # (node, col)
        q.append((root, 0))
        
        while q:
            for i in range(len(q)):
                node, col = q.popleft()
                if col not in col_to_topnode:
                    col_to_topnode[col] = node.data
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
        ans = []
        for col in sorted(col_to_topnode.keys()):
            ans.append(col_to_topnode[col])
        return ans