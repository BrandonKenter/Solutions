"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return root
        q = deque([root])
        
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            for i in range(len(level) - 1):
                level[i].next = level[i+1]
        return root
        