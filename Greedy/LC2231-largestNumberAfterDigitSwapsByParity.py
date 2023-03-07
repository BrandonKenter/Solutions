class Solution:
    def largestInteger(self, num: int) -> int:
        even_indices, odd_indices = [], []
        even_nums, odd_nums = [], []
        num = str(num)
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                even_indices.append(i)
                even_nums.append(int(num[i]))
            else:
                odd_indices.append(i)
                odd_nums.append(int(num[i]))
        even_nums.sort()
        odd_nums.sort()
        res = []
        i = j = 0
        while i < len(even_indices) and j < len(odd_indices):
            if even_indices[i] < odd_indices[j]:
                res.append(str(even_nums.pop()))
                i += 1
            else:
                res.append(str(odd_nums.pop()))
                j += 1
        if even_nums:
            res.extend(reversed([str(n) for n in even_nums]))
        elif odd_nums:
            res.extend(reversed([str(n) for n in odd_nums]))
        print(res)
        return int("".join(res))
        