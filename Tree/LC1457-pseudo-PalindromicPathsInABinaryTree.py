# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        counts = defaultdict(int)
        palCounts = 0

        def preorder(cur):
            nonlocal palCounts
            if cur is None:
                return
            
            counts[cur.val] += 1
            if not cur.left and not cur.right:
                oddCount = 0
                for _, count in counts.items():
                    if count % 2:
                        oddCount += 1
                if oddCount <= 1:
                    palCounts += 1
            preorder(cur.left)
            preorder(cur.right)
            counts[cur.val] -= 1
        
        preorder(root)
        return palCounts