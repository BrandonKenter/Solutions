# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(cur, r, c):
            if cur is None:
                return
            
            col_to_row[c].append((r, cur.val))
            dfs(cur.left, r+1, c-1)
            dfs(cur.right, r+1, c+1)

        col_to_row = defaultdict(list)
        dfs(root, 0, 0)
        ans = []
        for col in sorted(col_to_row.keys()):
            rows = col_to_row[col]
            rows.sort(key=lambda x:x[0])
            col_list = []

            for row in rows:
                col_list.append(row[1])
            ans.append(col_list)
        return ans
        