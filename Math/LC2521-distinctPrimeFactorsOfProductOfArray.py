'''
TLE
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        nums.sort()
        s = 1
        for i in range(len(nums)): s *= nums[i]

        count, i = 0, 2
        while s != 1:
            if self.is_prime(i) and s % i == 0:
                while s % i == 0:
                    s //= i
                count += 1
            i += 1
        return count
    
    def is_prime(self, n):
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True

'''
Better
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            t = 2
            while t * t <= x:
                while x % t == 0:
                    x //= t
                    s.add(t)
                t += 1
            if x > 1:
                s.add(x)
        return len(s)
