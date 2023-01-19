# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
BFS
'''
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = {0}
        self.q = deque([(0, root)])
        while self.q:
            for i in range(len(self.q)):
                cur_val, cur_node = self.q.popleft()
                if cur_node.left: 
                    left_val = cur_val * 2 + 1
                    self.q.append([left_val, cur_node.left])
                    self.values.add(left_val)
                if cur_node.right:
                    right_val = cur_val * 2 + 2
                    self.q.append([right_val, cur_node.right])
                    self.values.add(right_val)

    def find(self, target: int) -> bool:
        return target in self.values

'''
DFS
'''
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        def dfs(cur, val):
            if cur is None:
                return
            self.values.add(val)
            dfs(cur.left, val * 2 + 1)
            dfs(cur.right, val * 2 + 2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
