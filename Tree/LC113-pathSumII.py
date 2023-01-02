class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        
        def dfs(cur, path_sum, path):
            if cur is None:
                return
            
            path_sum += cur.val
            path.append(cur.val)
            if not cur.left and not cur.right and path_sum == targetSum:
                ans.append(path[::])
                
            dfs(cur.left, path_sum, path)
            dfs(cur.right, path_sum, path)
            
            path_sum -= cur.val
            path.pop()
        dfs(root, 0, [])
        return ans