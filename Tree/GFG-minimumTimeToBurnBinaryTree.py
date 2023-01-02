class Solution:
    def minTime(self, root,target):
        def findNode(root): 
            if root == None:
                return None
            if root.data == target:
                return root
            return findNode(root.left) or findNode(root.right)
            
        def parent_check(): 
            q = deque()
            q.append(root)
            
            while q:
                node = q.popleft()
                if node.left != None:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right != None:
                    parent[node.right] = node
                    q.append(node.right)

        parent = {}
        parent_check()
        visited = {} 
        q = deque()
        insert = findNode(root)
        q.append(insert)
        visited[insert] = True
        ans = 0

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
                if node.left != None and node.left not in visited:
                    q.append(node.left)
                    visited[node.left] = True
                if node.right != None and node.right not in visited:
                    q.append(node.right)
                    visited[node.right] = True
                if node in parent and parent[node] not in visited:
                    q.append(parent[node])
                    visited[parent[node]] = True
            ans += 1
        return ans-1 