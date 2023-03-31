# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Recursion
'''
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        suc = None
        
        def dfs(cur):
            nonlocal suc
            if cur is None:
                return
            
            if cur.val <= p.val:
                dfs(cur.right)
            else:
                suc = cur
                dfs(cur.left)
        dfs(root)
        return suc

    
'''
Iteration
'''
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        suc = None
        
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                suc = root
                root = root.left
        return suc
    