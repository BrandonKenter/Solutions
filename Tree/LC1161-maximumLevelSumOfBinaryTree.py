# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxiLevel = 0
        maxiSum = float('-inf')
        q = deque([root])
        curLevel = 1
        while q:
            levelSum = 0
            for i in range(len(q)):
                cur = q.popleft()
                levelSum += cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            if levelSum > maxiSum:
                maxiSum = levelSum
                maxiLevel = curLevel
            curLevel += 1
        return maxiLevel
