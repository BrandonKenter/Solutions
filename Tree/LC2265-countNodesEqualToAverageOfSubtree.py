class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(cur):
            nonlocal count
            if cur is None:
                return [0, 0] # [subtree sum, number of nodes in subtree]
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            
            subtree_sum = left[0] + right[0] + cur.val
            subtree_node_count = left[1] + right[1] + 1
            if cur.val == subtree_sum // subtree_node_count:
                count += 1
            return [subtree_sum, subtree_node_count]
        dfs(root)
        return count