class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt_sum = 0
        
        def dfs(cur):
            nonlocal tilt_sum
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            tilt_sum += (abs(left - right))
            return cur.val + left + right
        dfs(root)
        return tilt_sum