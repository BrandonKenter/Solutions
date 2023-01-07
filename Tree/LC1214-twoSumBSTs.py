# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Recursive
O(N+M) time / O(N) space
N is the number of nodes in root1 tree and M is the number of nodes in root2 tree
'''
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        vis = set()
        
        def fill(cur):
            if cur is None:
                return
            
            vis.add(cur.val)
            fill(cur.left)
            fill(cur.right)

        def find_twoSum(cur):
            if cur is None:
                return False
            
            if target - cur.val in vis:
                return True
            return find_twoSum(cur.left) or find_twoSum(cur.right)
        fill(root1)
        return find_twoSum(root2)


'''
Iterative Two Stacks
O(N+M) time / O(2H) space
N is the number of nodes in root1 tree and M is the number of nodes in root2 tree
'''
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        stack1 = []
        stack2 = []

        def get_stack1_next():
            if not stack1: return None
            root = stack1.pop()
            cur = root.right
            while cur:
                stack1.append(cur)
                cur = cur.left
            return root

        def get_stack2_next():
            if not stack2: return None
            root = stack2.pop()
            cur = root.left
            while cur:
                stack2.append(cur)
                cur = cur.right
            return root

        while root1:
            stack1.append(root1)
            root1 = root1.left
        
        while root2:
            stack2.append(root2)
            root2 = root2.right
        
        node1, node2 = get_stack1_next(), get_stack2_next()
        while node1 and node2:
            if node1.val + node2.val == target:
                return True
            elif node1.val + node2.val < target:
                node1 = get_stack1_next()
            else:
                node2 = get_stack2_next()
        return False
