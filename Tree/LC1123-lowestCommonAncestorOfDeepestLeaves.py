# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        lcs = None

        def dfs(cur, cur_depth):
            nonlocal max_depth, lcs
            if cur is None:
                return cur_depth

            left = dfs(cur.left, cur_depth + 1)
            right = dfs(cur.right, cur_depth + 1)
            max_depth = max(max_depth, left, right)
            if left == right == max_depth:
                lcs = cur
            return max(left, right)
        dfs(root, 0)
        return lcs