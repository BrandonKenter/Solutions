# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(cur):
            if not cur:
                return
            
            inorder(cur.left)
            res.append(cur.val)
            inorder(cur.right)
        
        inorder(root)
        return res