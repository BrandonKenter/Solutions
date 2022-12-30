class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = 0

        def dfs(cur, parent, grand):
            nonlocal s
            if cur is None:
                return

            if grand: s += cur.val
            grand = parent
            parent = cur.val % 2 == 0

            dfs(cur.left, parent, grand)
            dfs(cur.right, parent, grand)
        dfs(root, False, False)
        return s