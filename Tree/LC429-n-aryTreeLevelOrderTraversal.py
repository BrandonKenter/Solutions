"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        res = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                curNode = q.popleft()
                level.append(curNode.val)
                for neiNode in curNode.children:
                    q.append(neiNode)
            res.append(level)
        return res
