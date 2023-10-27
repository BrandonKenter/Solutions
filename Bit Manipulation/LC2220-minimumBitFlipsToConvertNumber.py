'''
Compare bits between each number
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        curStart, curGoal, count = start, goal, 0
        while curStart or curGoal:
            startBit, goalBit = curStart & 1, curGoal & 1
            count += startBit ^ goalBit
            curStart >>= 1
            curGoal >>= 1
        return count

'''
XOR the numbers and count 1 bits
'''
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cur, count = start ^ goal, 0
        while cur:
            count += cur & 1
            cur >>= 1
        return count
