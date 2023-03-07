# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        max_avg = 0

        def dfs(cur):
            nonlocal max_avg
            if cur is None:
                return [0, 0] # [num nodes, sum]
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            num_nodes, sub_sum = 1 + left[0] + right[0], cur.val + left[1] + right[1]
            max_avg = max(max_avg, (sub_sum / num_nodes))
            return [num_nodes, sub_sum]
        dfs(root)
        return max_avg
        