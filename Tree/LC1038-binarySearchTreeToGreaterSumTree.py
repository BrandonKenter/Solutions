class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        right_sum = 0

        def dfs(cur):
            nonlocal right_sum
            if cur is None:
                return 0
            
            dfs(cur.right)
            right_sum += cur.val
            cur.val = right_sum
            dfs(cur.left)
        dfs(root)
        return root