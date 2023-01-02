'''
Iterative
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        while root:
            if root.val == val:
                return root
            
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return None

'''
Recursive
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(cur):
            if cur is None:
                return None
            if cur.val == val:
                return cur
            
            if val < cur.val:
                return dfs(cur.left)
            else:
                return dfs(cur.right)
        return dfs(root)