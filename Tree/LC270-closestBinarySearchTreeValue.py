# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_val = -1
        closest_dif = float('inf')

        def dfs(cur):
            nonlocal closest_val, closest_dif
            if cur is None:
                return
            
            if abs(target - cur.val) <= closest_dif:
                closest_dif = abs(target - cur.val)
                closest_val = cur.val
            
            if target < cur.val:
                dfs(cur.left)
            else:
                dfs(cur.right)
        dfs(root)
        return closest_val
