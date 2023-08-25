# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        paths = 0

        def preorder(cur, curSum):
            nonlocal paths
            if cur is None:
                return
            
            curSum += cur.val
            paths += prefixSums[curSum - targetSum]
            prefixSums[curSum] += 1
            preorder(cur.left, curSum)
            preorder(cur.right, curSum)
            prefixSums[curSum] -= 1
        
        preorder(root, 0)
        return paths
        