# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        curLevel = 0

        while q:
            prev = None
            for _ in range(len(q)):
                curNode = q.popleft()
                if curLevel % 2 == 0:
                    if curNode.val % 2 == 0:
                        return False
                    elif prev:
                        if prev >= curNode.val:
                            return False
                    prev = curNode.val
                else:
                    if curNode.val % 2 == 1:
                        return False
                    elif prev:
                        if prev <= curNode.val:
                            return False
                    prev = curNode.val
                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            curLevel += 1
        return True
