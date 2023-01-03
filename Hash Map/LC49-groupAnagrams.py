class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            char_counts = [0] * 26
            for char in str:
                char_counts[ord(char) - ord('a')] += 1
            anagrams[tuple(char_counts)].append(str)
        return anagrams.values()