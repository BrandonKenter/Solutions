class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        i, prev = 0, -1
    
        while i < len(s):
            num_arr = []
            while i < len(s) and s[i].isnumeric():
                num_arr.append(s[i])
                i += 1
            if num_arr:
                num = int("".join(num_arr))
                if num <= prev:
                    return False
                prev = num
            i += 1
        return True