class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                prev = strs[j-1]
                cur = strs[j]
                if prev[i] > cur[i]:
                    count += 1
                    break
        return count
                