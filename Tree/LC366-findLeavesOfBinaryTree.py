class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def dfs(cur):
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            level = 1 + max(left, right)
            levels[level].append(cur.val)
            return level
        dfs(root)
        return levels.values()