# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def dfs(cur):
            if cur is None:
                return 0

            nonlocal max_path
            left = dfs(cur.left)
            left = left if left >= 0 else 0
            right = dfs(cur.right)
            right = right if right >= 0 else 0
            max_path = max(max_path, cur.val + left + right)
            return max(cur.val + left, cur.val + right)
        dfs(root)
        return max_path