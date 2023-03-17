class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        pre_counts = []
        count = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            pre_counts.append(count)
        
        res = []
        for l, r in queries:
            l_count = pre_counts[l-1] if l > 0 else 0 
            res.append(pre_counts[r] - l_count)
        return res
        