'''
Traversal - O(N) time / O(1) space
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p, length = len(s) - 1, 0

        while p >= 0:
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length
            p -= 1

        return length

'''
Split - O(N) time / O(N) space
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])