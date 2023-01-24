# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_counts = defaultdict(int)
        max_freq = 0

        def dfs(cur):
            nonlocal max_freq
            if cur is None:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            cur_sum = left + right + cur.val
            sum_counts[cur_sum] += 1
            max_freq = max(max_freq, sum_counts[cur_sum])
            return cur_sum
        
        dfs(root)
        return [s for s, count in sum_counts.items() if count == max_freq]