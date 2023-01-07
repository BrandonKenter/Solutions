# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        vis = set()

        def dfs(cur):
            if cur is None:
                return False
            
            if target - cur.val in vis:
                return True
            vis.add(cur.val)
            return dfs(cur.left) or dfs(cur.right)
        
        dfs(root1)
        return dfs(root2)