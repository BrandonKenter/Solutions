class Solution:
    def bottomView(self, root):
        if not root: return
        col_to_rows = defaultdict(list)
        q = deque() # Stores (node, row, col)
        q.append((root, 0, 0))
        
        while q:
            for i in range(len(q)):
                node, row, col = q.popleft()
                col_to_rows[col].append((row, node.data))
                
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))
                    
        ans = []
        for col in sorted(col_to_rows.keys()):
            rows = col_to_rows[col]
            ans.append(rows[-1][1])
        return ans