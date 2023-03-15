# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur, h, i):
            nonlocal count, last_i, max_h
            if cur is None:
                return
            
            count += 1
            if h > max_h:
                max_h = h
            if h == max_h:
                last_i = i
            dfs(cur.left, h+1, 2*i+1)
            dfs(cur.right, h+1, 2*i+2)
        
        count, last_i, max_h = 0, 0, 0
        dfs(root, 0, 0)
        return count - 1 == last_i
