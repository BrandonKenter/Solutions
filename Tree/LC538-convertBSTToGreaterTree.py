# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        right_sum = 0

        def dfs(cur):
            nonlocal right_sum
            if cur is None:
                return 0
            
            dfs(cur.right)
            right_sum += cur.val
            cur.val = right_sum
            dfs(cur.left)
            
        dfs(root)
        return root
