class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_1 = []
        leaves_2 = []

        def dfs(cur, leaves):
            if cur is None:
                return
            
            if not cur.left and not cur.right:
                leaves.append(cur.val)
            dfs(cur.left, leaves)
            dfs(cur.right, leaves)

        dfs(root1, leaves_1)
        dfs(root2, leaves_2)
        return leaves_1 == leaves_2