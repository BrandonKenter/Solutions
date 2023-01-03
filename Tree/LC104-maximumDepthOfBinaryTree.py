'''
DFS - O(N) time / O(H) space
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''
BFS - O(N) time / O(N) space
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                cur = q.popleft()

                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            level += 1
        return level