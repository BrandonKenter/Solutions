# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(cur):
            nonlocal count
            if not cur:
                return True
            
            l, r = dfs(cur.left), dfs(cur.right)
            
            if (
                l and r and 
                (not cur.left or cur.left.val == cur.val) and 
                (not cur.right or cur.right.val == cur.val)
            ):
                count += 1
                return True
            return False
        
        dfs(root)
        return count