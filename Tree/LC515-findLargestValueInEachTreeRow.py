# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        q = deque([root])

        while q:
            maxi = float('-inf')
            for i in range(len(q)):
                cur = q.popleft()
                maxi = max(maxi, cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(maxi)
        return res
    