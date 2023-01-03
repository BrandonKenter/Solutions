class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = defaultdict(int)

        starts = []
        l = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            if s_count == p_count:
                starts.append(l)
            if r >= len(p) - 1:
                s_count[s[l]] -= 1
                if s_count[s[l]] == 0:
                    s_count.pop(s[l])
                l += 1
        return starts