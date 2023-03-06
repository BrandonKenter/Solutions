class Solution:
    def smallestNumber(self, num: int) -> int:
        num_counts = Counter(str(abs(num)))
        res = []
        if num > 0:
            for num, count in sorted(num_counts.items()):
                if num == '0': continue
                res.append(num * count)
            smallest = "".join(res)
            smallest = smallest[:1] + '0' * num_counts['0'] + smallest[1:]

            return int(smallest)
        else:
            for num, count in sorted(num_counts.items(), reverse=True):
                res.append(num * count)
            smallest = "".join(res)
            return -1 * int(smallest)
            