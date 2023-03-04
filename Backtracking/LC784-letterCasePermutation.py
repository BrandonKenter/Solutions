class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        # Initialize result collection
        res = []
        # Initialize state collection
        perm = []

        # Create backtracking method
        def backtrack(i):
            if i == n:
                res.append("".join(perm))
                return
            
            if s[i].isnumeric():
                perm.append(s[i])
                backtrack(i+1)
                perm.pop()
            else:
                for c in [s[i].lower(), s[i].upper()]:         
                    perm.append(c)
                    backtrack(i+1)
                    perm.pop()

        backtrack(0)
        return res
