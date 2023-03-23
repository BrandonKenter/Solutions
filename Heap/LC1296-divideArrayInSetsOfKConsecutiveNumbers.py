'''
Hash map
Inefficient because of min(s.keys())
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = Counter(nums)
        while s:
            mini = min(s.keys())
            for i in range(k):
                if mini + i in s:
                    s[mini+i] -= 1
                    if s[mini+i] == 0:
                        s.pop(mini+i)
                else:
                    return False
        return True


'''
Heap + Hash map
'''
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        min_h = [num for num in counts.keys()]
        heapify(min_h)
        while min_h:
            first = min_h[0]
            for i in range(first, first + k):
                if i in counts:
                    counts[i] -= 1
                    if counts[i] == 0:
                        if i != min_h[0]:
                            return False
                        heappop(min_h)
                else:
                    return False
        return True
