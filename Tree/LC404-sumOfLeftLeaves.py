# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0

        def dfs(cur, left):
            nonlocal left_sum
            if cur is None:
                return 
            
            if not cur.left and not cur.right and left:
                left_sum += cur.val
            
            dfs(cur.left, True)
            dfs(cur.right, False)

        dfs(root, False)
        return left_sum