'''
Cast integers to bin
Interviewer likely will not be satisfied with this solution
O(1) time / O(1) space
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        maxi = max(len(a), len(b), len(c))
        a = '0' * (maxi - len(a)) + a
        b = '0' * (maxi - len(b)) + b
        c = '0' * (maxi - len(c)) + c
        cnt = 0
        for i, bit in enumerate(c):
            if bit == '0':
                if a[i] == '1': cnt += 1
                if b[i] == '1': cnt += 1
            else:
                if a[i] == '0' and b[i] == '0':
                    cnt += 1
        return cnt


'''
Bit manipulation
O(1) time / O(1) space
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while(a or b or c):
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    cnt += 1
            else:
                if bit_a == 1 and bit_b == 1:
                    cnt += 2
                elif bit_a or bit_b:
                    cnt += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return cnt
