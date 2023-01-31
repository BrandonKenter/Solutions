'''
While loop
O(2N) time / O(1) space
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while True:
            if i % 2 == 0 and i % n == 0:
                return i
            i += 1


'''
Pick between n and n * 2
O(1) time / O(1) space
'''
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2