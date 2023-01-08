# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = float('-inf')
        min_level = 0
        q = deque([root])

        level = 1
        while q:
            level_sum = 0
            for i in range(len(q)):
                cur = q.popleft()
                level_sum += cur.val

                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)

            if level_sum > max_level_sum:
                min_level = level
                max_level_sum = level_sum
            level += 1
        return min_level