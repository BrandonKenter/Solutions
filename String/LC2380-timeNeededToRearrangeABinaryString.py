class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = [char for char in s]
        seconds = 0
        while True:
            swapped = False
            i = 0
            while i < len(s) - 1:
                if s[i] == "0" and s[i+1] == "1":
                    s[i], s[i+1] = s[i+1], s[i]
                    swapped = True
                    i += 2
                else:
                    i += 1
            if swapped:
                seconds += 1
            else:
                return seconds
                