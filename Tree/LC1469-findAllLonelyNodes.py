class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely = []

        def dfs(cur):
            if cur is None:
                return

            if cur.left and not cur.right:
                lonely.append(cur.left.val)
            if cur.right and not cur.left:
                lonely.append(cur.right.val)
            
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return lonely