# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        old_to_new = {None : None}

        def dfs_left_right(old):
            if old is None:
                return None

            new = NodeCopy(old.val)
            old_to_new[old] = new
            new.left = dfs_left_right(old.left)
            new.right = dfs_left_right(old.right)
            return new
        
        def dfs_random(old):
            if old is None:
                return
            
            new = old_to_new[old]
            new.random = old_to_new[old.random]
            dfs_random(old.left)
            dfs_random(old.right)
        
        dfs_left_right(root)
        dfs_random(root)
        return old_to_new[root]