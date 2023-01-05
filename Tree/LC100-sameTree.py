# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
DFS - Recursive
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
DFS - Iterative
'''
class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            elif p or q:
                return False
        return True


'''
BFS
'''
class Solution:
    def isSameTree(self, p, q):
        def check(p, q):
            if not p and not q:
                return True
            if not q or not p or p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))      
        return True