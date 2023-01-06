'''
DFS
Traverses entire tree
Stores reference to the target clone in a variable
'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ref = None

        def dfs(original, cloned):
            nonlocal ref
            if original is None:
                return
            
            if original == target:
                ref = cloned
            else:
                dfs(original.left, cloned.left)
                dfs(original.right, cloned.right)
        dfs(original, cloned)
        return ref

'''
DFS
Returns early if found so doesn't have to traverse entire tree
Returns the reference to the target clone directly to caller
'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(root, clone):
            if not root:
                return None
            if root == target:
                return clone

            l = dfs(root.left, clone.left)
            r = dfs(root.right, clone.right)
            if l: return l
            if r: return r
        return dfs(original, cloned)
