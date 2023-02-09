# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node_counts = defaultdict(int)
        
        def dfs(cur):
            if cur is None:
                return
            
            node_counts[cur.val] += 1
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        max_count = max(node_counts.values())
        return [node[0] for node in node_counts.items() if node[1] == max_count]