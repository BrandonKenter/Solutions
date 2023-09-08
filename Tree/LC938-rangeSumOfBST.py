# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)

        s = root.val
        return s + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 

# Alternative using inorder traversal
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        def dfs(cur):
            nonlocal range_sum
            if cur is None:
                return
            
            if low <= cur.val <= high:
                range_sum += cur.val
            
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return range_sum
        
