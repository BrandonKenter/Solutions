'''
For this problem we can improve on the common approach of sorting, 
which takes O(Nlog(N)) time and O(N) space for Python's sort. To 
do this, we use bucket sort. We count the frequency of each char, 
put them in their respective frequency buckets, and greedily iterate 
backwards in the frequency bucket array so we choose the highest 
frequency chars first. Once we get to the 10th unique char, the 
number of keypresses we need to get to this char is incremented by 1.
To do this easily in 1 line we just multiply the frequency of the 
character by (math.ceil(used / 9)). So if used is 10, we multiply the 
frequency of the char by 2. Side note on bucket sort: we allocate 
len(s) space in the event that the whole string is made up of the 
same character.

Time: O(N)
Space: O(N)
'''
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = [[] for i in range(len(s) + 1)]
        counts = Counter(s)

        for char, count in counts.items():
            freq[count].append(char)
        
        keypresses = 0
        used = 0
        for i in range(len(s), -1, -1):
            for char in freq[i]:
                used += 1
                keypresses += i * (math.ceil(used / 9))
        return keypresses
