# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vis = set()

        def dfs(cur):
            nonlocal k
            if cur is None:
                return False
            
            if k - cur.val in vis:
                return True
            vis.add(cur.val)
            return dfs(cur.left) or dfs(cur.right)
        
        return dfs(root)
        