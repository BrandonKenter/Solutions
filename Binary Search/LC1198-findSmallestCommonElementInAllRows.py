class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for target in mat[0]:
            for i, row in enumerate(mat[1:]):
                left, right = 0, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] == target:
                        if i == m - 2:
                            return target
                        break
                    elif row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    break
        return -1
