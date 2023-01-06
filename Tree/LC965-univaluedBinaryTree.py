# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur, val):
            if cur is None:
                return True

            if cur.val != val:
                return False
            
            return dfs(cur.left, val) and dfs(cur.right, val)
        return dfs(root, root.val)