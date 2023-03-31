# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Recursive
Added return early logic (return when answer found)
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(cur):
            nonlocal kth, k
            if cur is None or kth:
                return
            
            dfs(cur.left)
            k -= 1
            if k == 0:
                kth = cur.val
            dfs(cur.right)
        
        kth = None
        dfs(root)
        return kth
    
    
'''
Recursive
Added return early logic (return when answer found)
Left and right return values instead of base case
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.v=0
        
        def inorder(node):
            if not node:
                return
            
            # left subtree
            l = inorder(node.left)
            if l is not None:
                return l
            # current node
            self.v+=1
            if self.v==k:
                return node.val
            
            # right subtree
            r = inorder(node.right)
            if r is not None:
                return r
        
        return inorder(root)


'''
Iterative
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
