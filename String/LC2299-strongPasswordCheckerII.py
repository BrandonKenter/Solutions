class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        lower = upper = digit = special = False
        for i in range(len(password)):
            char = password[i]
            if char.islower(): lower = True
            if char.isupper(): upper = True
            if char.isnumeric(): digit = True
            if char.isalnum() == False: special = True
            if i < len(password) - 1 and char == password[i+1]: return False
        return lower and upper and digit and special