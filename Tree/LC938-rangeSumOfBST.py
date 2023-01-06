# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        def dfs(cur):
            nonlocal range_sum
            if cur is None:
                return
            
            if low <= cur.val <= high:
                range_sum += cur.val
            
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return range_sum