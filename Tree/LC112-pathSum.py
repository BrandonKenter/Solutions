class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(cur, cur_sum):
            if cur is None:
                return False
            
            cur_sum += cur.val
            if not cur.left and not cur.right and cur_sum == targetSum:
                return True
            return dfs(cur.left, cur_sum) or dfs(cur.right, cur_sum)
        return dfs(root, 0)