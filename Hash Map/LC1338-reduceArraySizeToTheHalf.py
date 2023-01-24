'''
Array
O(N) time / O(N) space
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        freq = [[] for i in range(len(arr) + 1)]
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        
        for num, count in counts.items():
            freq[count].append(num)

        min_size = 0
        removed_elements = 0
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                min_size += 1
                removed_elements += i
                if removed_elements >= n // 2:
                    return min_size


'''
Hash map 
O(Nlog(N)) time / O(N) space
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1

        min_size = 0
        removed_elements = 0
        for num, count in sorted(counts.items(), key=lambda x : x[1], reverse=True):
            min_size += 1
            removed_elements += count
            if removed_elements >= n // 2:
                return min_size