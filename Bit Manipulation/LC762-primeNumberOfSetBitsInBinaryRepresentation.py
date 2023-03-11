'''
Casting to bin
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        primes = {2,3,5,7,11,13,17,19}
        for i in range(left, right+1):
            bits = bin(i).count('1')
            if bits in primes:
                count += 1           
        return count


'''
Bit manipulation
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        primes = {2,3,5,7,11,13,17,19}
        for i in range(left, right+1):
            c = 0
            while i:
                c += i & 1
                i >>= 1
            if c in primes:
                count += 1           
        return count
