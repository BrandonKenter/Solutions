class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_n = 0
        
        def dfs(cur, cur_m):
            nonlocal good_n
            if not cur:
                return
            
            if cur.val >= cur_m:
                good_n += 1
                cur_m = cur.val
            
            dfs(cur.left, cur_m)
            dfs(cur.right, cur_m)
        dfs(root, root.val)
        return good_n