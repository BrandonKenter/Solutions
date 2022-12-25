# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(cur, cur_path):
            if cur is None:
                return 
            
            cur_path.append(str(cur.val))
            if not cur.left and not cur.right:
                paths.append("->".join(cur_path[:]))
            dfs(cur.left, cur_path)
            dfs(cur.right, cur_path)
            cur_path.pop()
        
        dfs(root, [])
        return paths