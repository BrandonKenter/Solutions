class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)

        out = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                out.append(num)
                k -= 1
                if k == 0:
                    return out