# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            if left > right: return None

            # select the far right element as the root
            root_value = postorder.pop()
            root = TreeNode(root_value)

            # root splits inorder list
            # into left and right subtrees
            index = inorder_index_map[root_value]

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.right = array_to_tree(index + 1, right)
            root.left = array_to_tree(left, index - 1)

            return root

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(postorder) - 1)
