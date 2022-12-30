class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []

        def dfs(cur):
            if cur is None:
                return
            
            values.append(cur.val)
            for child in cur.children:
                dfs(child)
        dfs(root)
        return values