class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        cur_path = []
        s = 0

        def dfs(cur):
            nonlocal s
            if cur is None:
                return 
            
            cur_path.append(str(cur.val))
            if not cur.left and not cur.right:
                s += int("".join(cur_path), 2)
            dfs(cur.left)
            dfs(cur.right)
            cur_path.pop()
        dfs(root)
        return s