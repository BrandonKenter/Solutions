# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxi = 0

        def max_path(cur, is_left, path_len):
            nonlocal maxi
            if cur is None:
                return
            
            maxi = max(maxi, path_len)
            max_path(cur.left, True, path_len + 1 if not is_left else 1)
            max_path(cur.right, False, path_len + 1 if is_left else 1)
        
        max_path(root.left, True, 1)
        max_path(root.right, False, 1)
        return maxi
        