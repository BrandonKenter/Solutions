class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)

        for num in range(lowLimit, highLimit + 1):
            digit_sum = 0
            while num:
                digit = num % 10
                digit_sum += digit
                num //= 10
            boxes[digit_sum] += 1
        return max(boxes.values())