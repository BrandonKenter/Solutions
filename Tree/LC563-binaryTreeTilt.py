# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tiltSum = 0

        def postorder(cur):
            nonlocal tiltSum
            if cur is None:
                return 0
            
            left = postorder(cur.left)
            right = postorder(cur.right)
            tiltSum += abs(left - right)
            return left + right + cur.val
        
        postorder(root)
        return tiltSum
        