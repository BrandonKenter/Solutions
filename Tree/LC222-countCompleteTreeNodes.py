class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.get_left_height(root)
        right = self.get_right_height(root)

        if left == right: return (2 ** left) - 1
        else: return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def get_right_height(self, root):
        height = 0
        while root:
            height += 1
            root = root.right
        return height