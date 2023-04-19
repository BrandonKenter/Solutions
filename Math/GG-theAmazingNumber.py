class Solution:
    def isAmazing (self, n):
        count = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if i != n // 2: count += 2
                else: count += 1
        return 1 if count + 2 == 3 else 0
