class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        have = need = 0
        for c in t:
            if c not in t_count:
                need += 1
            t_count[c] += 1
        
        win_count = defaultdict(int)
        min_win_indices = [-1, -1]
        win_win_len = float('inf')
        l = 0
        for r in range(len(s)):
            win_count[s[r]] += 1
            if s[r] in t_count and t_count[s[r]] == win_count[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < win_win_len:
                    win_win_len = r - l + 1
                    min_win_indices = [l, r]
                win_count[s[l]] -= 1
                if win_count[s[l]] < t_count[s[l]]:
                    have -= 1
                if win_count[s[l]] == 0:
                    win_count.pop(s[l])
                l += 1
        i, j = min_win_indices
        return s[i:j + 1] if win_win_len != float('inf') else ""
