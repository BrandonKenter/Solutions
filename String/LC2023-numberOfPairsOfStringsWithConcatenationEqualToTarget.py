class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counts = Counter(nums)
        res = 0
        for pre, count in counts.items():
            if pre == target[:len(pre)]:
                suf = target[len(pre):]
                res += count * counts[suf]
                if pre == suf: res -= counts[suf]
        return res
