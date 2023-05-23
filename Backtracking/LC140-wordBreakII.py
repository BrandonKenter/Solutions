class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        cur_sentence = []

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur_sentence))
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    cur_sentence.append(s[i:j+1])
                    backtrack(j+1)
                    cur_sentence.pop()

        backtrack(0)
        return res
