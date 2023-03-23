'''
Lazy
Iterates from 2 to current n at every iteration
'''
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            start, cur = n, 0
            for i in range(2, start+1):
                while n % i == 0:
                    n //= i
                    cur += i
            if start == cur: return start
            n = cur


'''
More efficient
Manually divide out prime factor 2
Then iterate from 3 to sqrt(n) to get remaining odd prime factors
If we get all prime factors up to sqrt(n) and the reamining n > 2, this 
    means this is the last prime factor. It has to be the last prime factor
    because natural numbers n can be broken up into a unique set of prime 
    numbers that multiply together to get n. You can't multiple two numbers
    greater than sqrt(n) and get n because it will be larger than n. So, 
    only one prime factor will remain that is larger than sqrt(n) if this
    case is present.
'''
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            start, cur = n, 0
            while n % 2 == 0:
                n //= 2
                cur += 2
            for i in range(3, floor(sqrt(start)) + 1):
                while n % i == 0:
                    n //= i
                    cur += i
            if n > 2:
                cur += n
            if start == cur: return start
            n = cur
