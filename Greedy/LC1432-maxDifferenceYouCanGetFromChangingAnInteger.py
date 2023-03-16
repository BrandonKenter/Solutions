class Solution:
    def maxDiff(self, num: int) -> int:
        a = [d for d in str(num)]
        b = [d for d in str(num)]
        self.get_min(a)
        self.get_max(b)
        if len(a) == 1:
            a = ['1']
        return int("".join(b)) - int("".join(a))
        

    def get_max(self, a):
        a_replace = ''
        for i in range(len(a)):
            if i == 0:
                if a[i] != '9':
                    a_replace = a[i]
                    a[i] = '9'
            elif a[i] == a_replace:
                a[i] = '9'
            elif a_replace == '' and a[i] != '9':
                a_replace = a[i]
                a[i] = '9'


    def get_min(self, b):
        b_replace = ''
        r = ''
        for i in range(len(b)):
            if i == 0:
                if b[0] == '1':
                    continue
                else:
                    b_replace = b[i]
                    r = '1'
                    b[i] = r
            else:
                if b[i] == '1' and r == '':
                    continue
                elif b[i] == b_replace:
                    b[i] = r
                elif b_replace == ''and b[i] != '0':
                    b_replace = b[i]
                    r = '0'
                    b[i] = r
                elif b_replace == b[i]:
                    b[i] = r


'''
Way less code
'''
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxNum, minNum = float('-inf'), float('inf')
        for i in '0123456789':
            for j in '0123456789':
                nextNum = num.replace(i, j)
                if nextNum[0] == '0' or int(nextNum) == 0:
                    continue
                maxNum = max(maxNum, int(nextNum))    
                minNum = min(minNum, int(nextNum))    
        return maxNum - minNum 
        