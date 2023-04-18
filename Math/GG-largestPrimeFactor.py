class Solution:
    def largestPrimeFactor (self, N):
        maxi = 2
        num = N
        for i in range(2, int(sqrt(N)) + 1):
            while num % i == 0:
                num /= i
                maxi = i
        if num > 2:
            return int(num)
        else:
            return maxi
        