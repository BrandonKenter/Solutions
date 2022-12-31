'''
DFS
Not using hsh map
O(N) time / O(1) space
'''
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None: return None
        
        root_clone = Node(root.val)

        def dfs(cur, cur_clone):
            if cur is None:
                return

            for child in cur.children:
                child_clone = Node(child.val)
                cur_clone.children.append(child_clone)
                dfs(child, child_clone)
        dfs(root, root_clone)
        return root_clone
'''
DFS
Using hash map to map old node to clone node
O(N) time / O(N) space
'''
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None: return None

        root_clone = Node(root.val)
        old_to_clone = {root : root_clone}

        def dfs(cur):
            if cur is None:
                return
            
            for child in cur.children:
                child_clone = Node(child.val)
                old_to_clone[child] = child_clone
                old_to_clone[cur].children.append(child_clone)
                dfs(child)
        dfs(root)
        return old_to_clone[root]