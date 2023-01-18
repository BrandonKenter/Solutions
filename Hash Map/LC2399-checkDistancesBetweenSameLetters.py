class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        letter_indices = defaultdict(list)
        for i, char in enumerate(s):
            letter_indices[char].append(i)
        
        for i in range(26):
            char = chr(i + ord('a'))
            if char in letter_indices:
                index_1, index_2 = letter_indices[char]
                if index_2 - index_1 - 1 != distance[i]:
                    print(i)
                    return False
        return True