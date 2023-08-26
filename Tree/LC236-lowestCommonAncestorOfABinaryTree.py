# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def postorder(cur):
            if not cur:
                return None
            if cur == p or cur == q:
                return cur
            
            left = postorder(cur.left)
            right = postorder(cur.right)
            
            if left and right: return cur
            elif left: return left
            elif right: return right
            else: return None
            
        return postorder(root)
        