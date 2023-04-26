'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        
        def dfs(cur):
            if cur is None:
                return [True, 0]
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            child_sum = left[1] + right[1]
            equal_child = ((cur.left or cur.right) and child_sum == cur.data) or (not cur.left and not cur.right)
            return [left[0] and right[0] and equal_child, cur.data]
        
        return 1 if dfs(root)[0] else 0
        