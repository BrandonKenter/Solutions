class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sub_counts = defaultdict(int)
        for cp in cpdomains:
            count, dom = cp.split(" ")
            subs = dom.split(".")
            for i in range(len(subs) - 1, -1 ,-1):
                if i == len(subs) - 1:
                    sub_counts[subs[i]] += int(count)
                else:
                    sub_counts[".".join(subs[i:])] += int(count)
        
        res = []
        for sub, count in sub_counts.items():
            res.append(str(count) + " " + sub)
        return res
            