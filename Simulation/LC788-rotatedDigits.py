class Solution:
    def rotatedDigits(self, n: int) -> int:
        # rotation of n is valid if conditions are met and its different than n
        digit_set = set(['2', '5', '6', '9', '0', '1', '8'])
        m = {'2':'5','5':'2','6':'9','9':'6'}
        good_count = 0
        for num in range(1, n + 1):
            num = str(num)
            new_num = []
            for digit in num:
                if digit not in digit_set:
                    break
                if digit in m:
                    new_num.append(m[digit])
                else:
                    new_num.append(digit)
            else:
                if "".join(new_num) != num:
                    good_count += 1
        return good_count
