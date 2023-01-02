class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(1, root)])
        max_width = 0
        
        while q:
            left = q[0][0] # Leftmost node number in level
            for i in range(len(q)):
                right, node = q.popleft()
                max_width = max(max_width, right - left + 1)
                if node.left: q.append((right * 2, node.left))
                if node.right: q.append((right * 2 + 1, node.right))
        return max_width