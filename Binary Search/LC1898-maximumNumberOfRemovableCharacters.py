class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right) // 2
            new_s = []
            to_remove = set(removable[:mid + 1])
            for i, c in enumerate(s):
                if i not in to_remove:
                    new_s.append(c)
            new_s = "".join(new_s)
            i = j = 0
            while i < len(new_s) and j < len(p):
                if new_s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j < len(p):
                right = mid
            else:
                left = mid + 1
        return right
