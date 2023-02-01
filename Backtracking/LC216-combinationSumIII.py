class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, combo = [], []
        used = set()
        nums = [i for i in range(1, 10)]

        def backtrack(prev, cur_sum):
            if len(combo) == k and cur_sum == n:
                res.append(combo[:])
                return
            if len(combo) == k or cur_sum > n:
                return
            
            for i in range(prev + 1, 10):
                if i not in used:
                    used.add(i)
                    cur_sum += i
                    combo.append(i)

                    backtrack(i, cur_sum)

                    used.remove(i)
                    cur_sum -= i
                    combo.pop()
        backtrack(0, 0)
        return res