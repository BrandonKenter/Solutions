class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        count = 0
        for d in number:
            if d == digit: count += 1

        cur_count = 0
        for i in range(len(number)):
            if number[i] == digit:
                cur_count += 1
                if cur_count == count:
                    return number[:i] + number[i+1:]
                elif int(number[i+1]) > int(number[i]):
                    return number[:i] + number[i+1:]
