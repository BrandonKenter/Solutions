class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_counts = defaultdict(int)
        for char in licensePlate.lower():
            if char != ' ' and char.isnumeric() == False:
                license_counts[char] += 1

        short_license = ""
        for char, char_count in license_counts.items():
            short_license += (char * char_count)
        short_license_set = set(short_license)
        
        min_word = None
        min_len = float('inf')

        for word in words:
            word_set = set(word)
            if short_license_set.issubset(word_set) == False:
                continue

            word_counts = defaultdict(int)
            char_count_sum = 0
            for char in word:
                word_counts[char] += 1
                char_count_sum += 1
            
            for char, char_count in word_counts.items():
                if char_count < license_counts[char]:
                    char_count_sum = float('inf')
                    break
                    
            if char_count_sum < min_len:
                min_len = char_count_sum
                min_word = word
        return min_word