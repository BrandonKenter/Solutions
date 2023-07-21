# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(cur):
            nonlocal count
            if not cur:
                return True
            
            left, right = dfs(cur.left), dfs(cur.right)
            if left and right:
                if (
                    (cur.left and cur.left.val != cur.val) or
                    (cur.right and cur.right.val != cur.val)
                    ):
                    return False

                count += 1
                return True
            else:
                return False
            
        dfs(root)
        return count
