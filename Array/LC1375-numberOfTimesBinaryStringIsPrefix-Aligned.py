class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        total_zero = len(flips)
        pre_i = count = 0
        flipped = [0] * len(flips)
        for flip_i in flips:
            flip_i -= 1
            flipped[flip_i] = 1
            total_zero -= 1
            while pre_i < len(flips) and flipped[pre_i] == 1:
                pre_i += 1
            if flip_i < pre_i and total_zero == len(flips) - pre_i:
                count += 1
        return count
        