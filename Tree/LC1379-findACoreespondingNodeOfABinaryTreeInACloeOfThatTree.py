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
        def dfs(original, cloned):
            if original is None:
                return None
            
            if original == target:
                return cloned
            else:
                left = dfs(original.left, cloned.left)
                right = dfs(original.right, cloned.right)
                if left: return left
                elif right: return right
                else: return None
        return dfs(original, cloned)