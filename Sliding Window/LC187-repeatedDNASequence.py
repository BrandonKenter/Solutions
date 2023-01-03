class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        ans = set()

        l = 0
        for r in range(9, len(s)):
            cur_sequence = s[l:r + 1]
            if cur_sequence in seen:
                ans.add(cur_sequence)
            else:
                seen.add(cur_sequence)
            l += 1
        return list(ans)