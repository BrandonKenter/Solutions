class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        m = {i : v for i, v in enumerate(mapping)}
        pairs = []
        for i, num in enumerate(nums):
            num_arr = []
            for d in str(num):
                num_arr.append(str(m[int(d)]))
            num_s = int("".join(num_arr))
            pairs.append((num_s, i, num))
        return [pair[2] for pair in sorted(pairs)]
        