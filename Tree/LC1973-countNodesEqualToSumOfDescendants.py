# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(cur):
            nonlocal count
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            desc_sum = left + right
            if desc_sum == cur.val: count += 1

            return cur.val + left + right
        dfs(root)
        return count