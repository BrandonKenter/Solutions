class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_to_word = {}
        for word in words:
            symbols = []
            for char in word:
                symbols.append(morse[ord(char) - ord('a')])
            morse_to_word["".join(symbols)] = word
        return len(morse_to_word)