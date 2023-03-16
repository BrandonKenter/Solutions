# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = None
            for _ in range(len(q)):
                cur = q.popleft()
                if level % 2 == 0:
                    if cur.val % 2 == 0:
                        return False
                    if prev:
                        if prev >= cur.val:
                            return False
                    prev = cur.val
                else:
                    if cur.val % 2 == 1:
                        return False
                    if prev:
                        if prev <= cur.val:
                            return False
                    prev = cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            level += 1
        return True
