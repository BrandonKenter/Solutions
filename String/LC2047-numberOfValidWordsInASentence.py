class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0
        for word in words:
            if self.is_valid(word):
                count += 1
        return count
        
    def is_valid(self, word):
        punctuation = {'!', '.', ','}
        hyphen_count = 0
        for i in range(len(word)):
            c = word[i]
            if c.isalpha() and c.isupper() or c.isnumeric():
                return False
            if c == '-':
                hyphen_count += 1
                if hyphen_count > 1:
                    return False
                if i == 0 or i == len(word) - 1 or word[i-1].isalpha() == False or word[i+1].isalpha() == False:
                    return False
            if c in punctuation:
                if i != len(word) - 1:
                    return False
        return True
