class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_num, second_num, target_num = [], [], []
        for char in firstWord: 
            first_num.append(str(ord(char) - ord('a')))
        first_num = int("".join(first_num))
        for char in secondWord: 
            second_num.append(str(ord(char) - ord('a')))
        second_num = int("".join(second_num))
        for char in targetWord: 
            target_num.append(str(ord(char) - ord('a')))
        target_num = int("".join(target_num))
        return first_num + second_num == target_num