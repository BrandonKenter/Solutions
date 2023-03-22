class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        original = perm[:]
        ops = 0
        while True:
            arr = perm[:]
            for i in range(len(perm)):
                if i % 2 == 0: arr[i] = perm[i // 2]
                if i % 2 == 1: arr[i] = perm[n // 2 + (i - 1) // 2]
            ops += 1
            if arr == original:
                return ops
            else:
                perm = arr
            