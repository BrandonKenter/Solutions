# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(cur, path):
            c = chr(ord('a') + cur.val)
            if not cur.left and not cur.right:
                return c + path
            if cur.left is None:
                return dfs(cur.right, c + path)
            if cur.right is None:
                return dfs(cur.left,  c + path) 
            return min(dfs(cur.left, c + path), dfs(cur.right, c + path))
        return dfs(root, '')
        