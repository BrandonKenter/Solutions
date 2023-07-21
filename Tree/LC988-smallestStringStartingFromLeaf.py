# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(cur, path):
            if cur is None:
                return 'zzzzz'
                
            c = chr(ord('a') + cur.val)
            if not cur.left and not cur.right:
                return c + path
                
            left = dfs(cur.right, c + path)
            right = dfs(cur.left,  c + path) 
            return min(left, right)
        return dfs(root, '')
        
