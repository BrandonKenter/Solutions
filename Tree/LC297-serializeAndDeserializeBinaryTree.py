class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None: return ""

        q = deque([root])
        res = []

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if not cur:
                    res.append("N")
                    continue
                
                res.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
        return ",".join(res)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])
        
        i = 1
        while q and i < len(values):
            parent = q.popleft()
            if values[i] != "N":
                left = TreeNode(int(values[i]))
                parent.left = left
                q.append(left)
            i += 1
            if values[i] != "N":
                right = TreeNode(int(values[i]))
                parent.right = right
                q.append(right)
            i += 1
        return root