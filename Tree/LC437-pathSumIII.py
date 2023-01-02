class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_map = defaultdict(int)
        count = 0

        def dfs(cur, cur_sum):
            nonlocal count
            if cur is None:
                return

            cur_sum += cur.val
            if cur_sum == targetSum:
                count += 1

            count += prefix_map[cur_sum - targetSum]
            prefix_map[cur_sum] += 1

            dfs(cur.left, cur_sum)
            dfs(cur.right, cur_sum)

            prefix_map[cur_sum] -= 1

        dfs(root, 0)
        return count