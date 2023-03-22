class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divs = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divs.add(i)
                    divs.add(num // i)
            if len(divs) == 4:
                res += sum(divs)
        return res
        