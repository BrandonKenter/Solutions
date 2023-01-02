class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        col_to_rows = defaultdict(list)
        q = deque() # (node, row, col)
        q.append((root, 0, 0))
        
        while q:
            for i in range(len(q)):
                node, row, col = q.popleft()
                col_to_rows[col].append((row, node.val))

                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))

        ans = []
        for col in sorted(col_to_rows.keys()):
            rows = col_to_rows[col]
            rows.sort()
            col_list = []

            for row in rows:
                col_list.append(row[1])
            ans.append(col_list)
        return ans