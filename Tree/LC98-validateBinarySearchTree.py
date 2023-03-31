# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur, mini, maxi):
            if cur is None:
                return True
            
            if cur.val <= mini or cur.val >= maxi:
                return False
            left = dfs(cur.left, mini, cur.val)
            right = dfs(cur.right, cur.val, maxi)
            return left and right
        
        return dfs(root, float('-inf'), float('inf'))
        