class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0

        def dfs(cur):
            nonlocal tilt
            if cur is None:
                return 0

            left = dfs(cur.left)
            right = dfs(cur.right)

            node_tilt = abs(left - right)
            tilt += node_tilt
            return left + right + cur.val
        dfs(root)
        return tilt
