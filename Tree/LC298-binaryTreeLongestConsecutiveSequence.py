# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_seq = 0

        def dfs(cur, parent, seq):
            nonlocal max_seq
            if cur is None:
                return 
            
            if parent and parent.val == cur.val - 1:
                seq += 1
            else:
                seq = 1
            max_seq = max(max_seq, seq)

            dfs(cur.left, cur, seq)
            dfs(cur.right, cur, seq)
        
        dfs(root, None, 0)
        return max_seq
        