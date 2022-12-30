class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first_min = root.val
        second_min = float('inf')

        def dfs(cur):
            nonlocal first_min, second_min
            if cur is None:
                return
            
            if first_min < cur.val < second_min:
                second_min = cur.val
            else:
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)
        return second_min if second_min != float('inf') else -1