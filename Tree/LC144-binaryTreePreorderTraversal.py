# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(cur):
            if cur is None:
                return
            
            res.append(cur.val)
            preorder(cur.left)
            preorder(cur.right)
        preorder(root)
        return res