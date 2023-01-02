class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        if not root.left and not root.right:
            return res
        self.get_left(root.left, res)
        self.get_leaves(root, res)
        self.get_right(root.right, res)
        return res

    def is_leaf(self, cur):
            if not cur.left and not cur.right:
                return True
            return False

    def get_left(self, root, res):
        
        def dfs(cur):
            if cur is None:
                return
            
            if not self.is_leaf(cur): res.append(cur.val)
            if cur.left: dfs(cur.left)
            else: dfs(cur.right)
        dfs(root)
    
    def get_leaves(self, root, res):
        
        def dfs(cur):
            if cur is None:
                return
            
            if self.is_leaf(cur):
                res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)

    def get_right(self, root, res):
        stack = []

        def dfs(cur):
            if cur is None:
                return
            
            if not self.is_leaf(cur): stack.append(cur.val)
            if cur.right: dfs(cur.right)
            else: dfs(cur.left)
            
        dfs(root)
        while stack:
            res.append(stack.pop())