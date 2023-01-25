'''
Two loops
Traverse a chars, traverse b chars
'''
class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        while i < len(s) and s[i] == 'a':
            i += 1
        while i < len(s) and s[i] == 'b':
            i += 1
        return i == len(s)


'''
One loop
Check adjacent characters
'''
class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) == 1: 
            return True

        for i in range(1, len(s)):
            if s[i-1] == 'b' and s[i] == 'a': 
                return False
        return True