class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        uniques = set()

        def overlap(s):
            prev = set()
            for c in s:
                if c in uniques or c in prev:
                    return True
                prev.add(c)
            return False

        def backtrack(i):
            nonlocal res
            if i == len(arr):
                res = max(res, len(uniques))
                return
            
            if not overlap(arr[i]):
                for char in arr[i]:
                    uniques.add(char)
                backtrack(i+1)
                for char in arr[i]:
                    uniques.remove(char)
            backtrack(i+1)
        
        backtrack(0)
        return res
        