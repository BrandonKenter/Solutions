'''
Iterative
'''
class Solution:
    def findCeil(self,root, inp):
        ceil = -1
        
        while root:
            if root.key >= inp:
                ceil = root.key
                root = root.left
            else:
                root = root.right
        return ceil

'''
Recursive
'''
class Solution:
    def findCeil(self,root, inp):
        ceil = -1
    
        def search(cur):
            nonlocal ceil
            if cur is None:
                return ceil
            
            if cur.key >= inp:
                ceil = cur.key
                return search(cur.left)
            else:
                return search(cur.right)
        return search(root)