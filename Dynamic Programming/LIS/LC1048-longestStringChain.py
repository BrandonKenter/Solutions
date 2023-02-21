class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def check(word1, word2):
            if len(word1) + 1 != len(word2): return False

            i = j = 0
            while j < len(word2):
                if i == len(word1):
                    return True

                if word1[i] == word2[j]:
                    i, j = i + 1, j + 1
                else:
                    j += 1
            return i == len(word1) and j == len(word2)
        
        words = sorted(words, key=len)
        n = len(words)
        maxi = 1
        dp = [1] * n

        for i in range(n):
            for prev in range(i):
                if check(words[prev], words[i]) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi