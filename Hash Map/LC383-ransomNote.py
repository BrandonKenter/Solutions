'''
Hash Map - O(N) time / O(N) space
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_counts = Counter(magazine)
        
        for c in ransomNote:
            if c not in mag_counts or mag_counts[c] == 0:
                return False
            mag_counts[c] -= 1
        return True

        
'''
Casting, Sorting and Two Pointers - O(Nlog(N)) time / O(N) space
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        ransomNote.sort()
        magazine = list(magazine)
        magazine.sort()

        i = 0
        j = 0
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(ransomNote)