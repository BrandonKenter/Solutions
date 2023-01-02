class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        
        def dfs(cur):
            nonlocal out
            if cur is None:
                return
            
            dfs(cur.left)
            out.append(cur.val)
            dfs(cur.right)
        dfs(root)
        return out