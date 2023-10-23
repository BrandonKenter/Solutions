'''
XOR full 1-bit mask
'''
class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)[2:])
        return (2 ** length - 1) ^ num

'''
XOR individual 1-bit mask left shift
'''
class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)[2:])
        for i in range(length):
            num ^= 1 << i
        return num

'''
XOR individual 1-bit mask right shift
'''
class Solution:
    def findComplement(self, num: int) -> int:
        cur, bit = num, 1
        while cur:
            num = num ^ bit
            bit = bit << 1
            cur = cur >> 1
        return num