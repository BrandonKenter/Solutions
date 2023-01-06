# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_dif = float('inf')
        prev = float('inf')

        def dfs(cur):
            nonlocal min_dif, prev
        
            if cur is None:
                return 

            dfs(cur.left)
            min_dif = min(min_dif, abs(cur.val - prev))
            prev = cur.val
            dfs(cur.right)
        
        dfs(root)
        return min_dif