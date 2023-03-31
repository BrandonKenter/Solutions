class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        vowels = {'a','e','i','o','u'}
        for i in range(len(word)):
            vowel_set = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                else:
                    vowel_set.add(word[j])
                    if len(vowel_set) == 5:
                        count += 1
        return count
        