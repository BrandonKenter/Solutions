# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_i = 0

        def dfs(cur, i):
            nonlocal max_i
            if cur is None:
                return
            
            max_i = max(max_i, i)
            dfs(cur.left, i * 2 + 1)
            dfs(cur.right, i * 2 + 2)
            
        dfs(root, 0)
        return max_i + 1
