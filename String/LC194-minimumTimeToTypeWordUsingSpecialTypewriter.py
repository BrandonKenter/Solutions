'''
Explicit cases
'''
class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = 'a'
        for char in word:
            time += 1
            char_i, prev_i = ord(char) - ord('a'), ord(prev) - ord('a')
            no_wrap = abs(char_i - prev_i)
            wrap_left = 25 - char_i + 1 + prev_i
            wrap_right = 25 - prev_i + 1 + char_i
            time += min(no_wrap, wrap_left, wrap_right)
            prev = char
        return time


'''
Modulo math
'''
class Solution:
    def minTimeToType(self, word: str) -> int:
        time = len(word)
        prev = "a"
        for char in word: 
            val = (ord(char) - ord(prev) + 26) % 26 # add 26 since we can get a negative
            time += min(val, 26 - val)
            prev = char
        return time 