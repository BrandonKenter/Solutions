class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one_count = 0
        for num in data: 
            if num == 1: one_count += 1 
        if one_count == 0: 
            return 0

        min_zeroes = float('inf')
        zero_count = left = 0
        for right in range(len(data)):
            if data[right] == 0:
                zero_count += 1
            
            if right - left + 1 == one_count:
                min_zeroes = min(min_zeroes, zero_count)
                if data[left] == 0:
                    zero_count -= 1
                left += 1
        return min_zeroes