# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def preorder(cur, depth):
            if not cur:
                return float('inf')
            if not cur.left and not cur.right:
                return depth
            
            left = preorder(cur.left, depth + 1)
            right = preorder(cur.right, depth + 1)
            return min(left, right)
        
        return preorder(root, 1)