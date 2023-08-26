# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxPathLen = 0

        def preorder(cur, isLeft, pathLen):
            nonlocal maxPathLen
            if cur is None:
                return
            
            maxPathLen = max(maxPathLen, pathLen)
            preorder(cur.left, True, pathLen + 1 if not isLeft else 1)
            preorder(cur.right, False, pathLen + 1 if isLeft else 1)
        
        preorder(root.left, True, 1)
        preorder(root.right, False, 1)
        return maxPathLen
        