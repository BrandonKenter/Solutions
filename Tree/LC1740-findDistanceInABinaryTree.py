# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self.getLCA(root, p, q)
        return self.getDist(lca, p) + self.getDist(lca, q)

    def getLCA(self, cur, p, q):
        if not cur:
            return None

        if cur.val == p or cur.val == q:
            return cur
        left = self.getLCA(cur.left, p, q)
        right = self.getLCA(cur.right, p, q)
        if left and right:
            return cur
        if left: return left
        if right: return right
        
    def getDist(self, cur, target):
        if cur is None:
            return float('inf')
        if cur.val == target:
            return 0
        return 1 + min(self.getDist(cur.left, target), self.getDist(cur.right, target))
