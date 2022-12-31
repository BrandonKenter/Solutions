class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level_height = 0
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur)

                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)

            if level_height % 2:
                left, right = 0, len(level) - 1
                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
            level_height += 1
        return root