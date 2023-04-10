# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(cur):
            if cur is None:
                return
            
            inorder(cur.left)
            arr.append(cur.val)
            inorder(cur.right)
        
        arr = []
        inorder(root)
        def build_tree(cur_arr):
            if not cur_arr:
                return None
            
            mid = len(cur_arr) // 2
            cur = TreeNode(cur_arr[mid])
            cur.left = build_tree(cur_arr[:mid])
            cur.right = build_tree(cur_arr[mid+1:])
            return cur
        
        new_root = build_tree(arr)
        return new_root
