# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
BFS - O(N) time / O(D) space
'''
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            level_len = len(q)
            for i in range(level_len):
                cur = q.popleft()
                if cur == u:
                    if i != level_len - 1 and q:
                        return q.popleft()
                    else:
                        return None
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)


'''
DFS - Preorder - O(N) time / O(H) space
'''
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        u_height, nearest = 0, None
        def dfs(cur, cur_height):
            nonlocal u_height, nearest
            if cur is None:
                return False
            
            cur_height += 1
            if cur == u:
                u_height = cur_height
                return False
            
            if cur_height == u_height:
                nearest = cur
                return True
            
            return dfs(cur.left, cur_height) or dfs(cur.right, cur_height)
        dfs(root, 0)
        return nearest