class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        uniques = set()
        maxi = 0

        def backtrack(i):
            nonlocal maxi
            if i == len(s):
                maxi = max(maxi, len(uniques))
                return
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub not in uniques:
                    uniques.add(sub)
                    backtrack(j+1)
                    uniques.remove(sub)
        
        backtrack(0)
        return maxi
        a