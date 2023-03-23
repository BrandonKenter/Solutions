# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        maxi = max(nums)
        root = TreeNode(maxi)
        maxi_i = nums.index(maxi)
        root.left = self.constructMaximumBinaryTree(nums[:maxi_i])
        root.right = self.constructMaximumBinaryTree(nums[maxi_i+1:])
        return root
