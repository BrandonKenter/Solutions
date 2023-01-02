'''
Iterative
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
        return root

'''
Recursive
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root):
            if val < root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = TreeNode(val)
        
        if not root: return TreeNode(val)
        dfs(root)
        return root