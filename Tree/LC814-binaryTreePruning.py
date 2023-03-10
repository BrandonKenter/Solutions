# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(cur):
            if cur is None:
                return
            
            cur.left = dfs(cur.left)
            cur.right = dfs(cur.right)
            if not cur.left and not cur.right and cur.val == 0:
                return None
            return cur
        
        return dfs(root)