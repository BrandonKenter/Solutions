class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l_set = set()
        r_counts = Counter(s)
        uniques = set() # (inner, outer)

        for char in s:
            r_counts[char] -= 1
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter in l_set and r_counts[letter]:
                    uniques.add((char, letter))
            l_set.add(char)
        return len(uniques)