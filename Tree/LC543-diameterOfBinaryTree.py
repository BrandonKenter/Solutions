# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0

        def dfs(cur):
            nonlocal max_diam
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            max_diam = max(max_diam, left + right)
            return 1 + max(left, right)
        dfs(root)
        return max_diam