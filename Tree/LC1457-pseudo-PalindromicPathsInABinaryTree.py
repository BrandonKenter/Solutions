# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        path_counts = defaultdict(int)
        pal_count = 0

        def dfs(cur):
            nonlocal pal_count
            if cur is None:
                return
            
            path_counts[cur.val] += 1
            if not cur.left and not cur.right:
                odd_count = 0
                for val, count in path_counts.items():
                    if count % 2: odd_count += 1
                if odd_count <= 1:
                    pal_count += 1
            dfs(cur.left)
            dfs(cur.right)
            path_counts[cur.val] -= 1
        
        dfs(root)
        return pal_count
        