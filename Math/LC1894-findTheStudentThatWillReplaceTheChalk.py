class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        k = k % s
        n, i = len(chalk), 0
        while True:
            k -= chalk[i%n]
            if k < 0:
                return i%n
            i += 1
