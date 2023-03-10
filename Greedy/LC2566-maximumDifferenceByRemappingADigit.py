class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)

        # Get max
        maxi = num[:]
        for c in num:
            if c != '9':
                maxi = maxi.replace(c, '9')
                print(maxi)
                break
        
        # Get min
        mini = num[:]
        for c in num:
            if c != '0':
                mini = mini.replace(c, '0')
                break
        
        return int(maxi) - int(mini)
