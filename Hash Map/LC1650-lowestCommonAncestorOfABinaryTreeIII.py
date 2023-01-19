"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
O(1) time / O(H) space
- Add nodes from path to root of either p or q using parent references
- Use parent references of other node up to root until we merge with other path
'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = set()

        while p:
            p_path.add(p)
            p = p.parent
        while q not in p_path:
            q = q.parent
        return q


'''
O(H) time / O(1) space
- Iterate from each node p and q to the root
- If we reach the root, we start from the opposite node's start position
- If there is a difference in length to the intersection, it takes 2 O(H) traversals
- It is guaranteed to be found in 1 or 2 traversals, making the time complexity O(H)
'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_cur, q_cur = p, q

        while p_cur != q_cur:
            p_cur = p_cur.parent if p_cur.parent else q
            q_cur = q_cur.parent if q_cur.parent else p
        return p_cur