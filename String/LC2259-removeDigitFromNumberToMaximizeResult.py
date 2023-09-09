class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        remove_i = -1
        mini = 10
        for i in range(len(number)):
            if number[i] == digit:
                if i < len(number) - 1 and number[i + 1] > number[i]:
                    remove_i = i
                    break
                else: 
                    remove_i = i
        
        return number[:remove_i] + number[remove_i + 1:]
        