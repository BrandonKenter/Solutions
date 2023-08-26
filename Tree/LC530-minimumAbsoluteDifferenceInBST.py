# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prevVal = None
        minDif = float('inf')
        
        def inorder(curNode):
            nonlocal prevVal, minDif
            if not curNode:
                return 
            
            inorder(curNode.left)
            if prevVal is not None: minDif = min(minDif, curNode.val - prevVal)
            prevVal = curNode.val
            inorder(curNode.right)
        
        inorder(root)
        return minDif
        