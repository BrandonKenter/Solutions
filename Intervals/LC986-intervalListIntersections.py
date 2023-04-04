class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = [] 
        while i < len(firstList) and j < len(secondList):
            first_s, first_e = firstList[i]
            second_s, second_e = secondList[j]
            
            # First interval is completely before second interval
            if first_e < second_s: 
                i += 1
            # Second interval is completely before first interval
            elif second_e < first_s:
                j += 1
            # There is some intersection
            else:
                new_start, new_end = max(first_s, second_s), min(first_e, second_e)
                res.append([new_start, new_end])
                # There is some part of the first interval left after intersection
                if new_end < first_e:
                    firstList[i][0] = new_start
                    j += 1
                # There is some part of the second interval left after intersection
                elif new_end < second_e:
                    secondList[j][0] = new_start
                    i += 1
                # There is no part of the intervals left after the intersection
                else:
                    i += 1
                    j += 1
            
        return res
