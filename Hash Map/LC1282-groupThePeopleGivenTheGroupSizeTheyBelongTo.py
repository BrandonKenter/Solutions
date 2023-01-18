class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list) # list of lists of group size
        for person, groupSize in enumerate(groupSizes):
            if len(groups[groupSize]) == 0 or len(groups[groupSize][-1]) == groupSize:
                groups[groupSize].append([person])
            else:
                groups[groupSize][-1].append(person)

        groupSizes = groups.values()
        res = []
        for groupSize in groupSizes:
            for group in groupSize:
                res.append(group)
        return res