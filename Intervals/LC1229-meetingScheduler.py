class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start_1, end_1 = slots1[i]
            start_2, end_2 = slots2[j]
            # First slot is before second slot
            if end_1 < start_2:
                i += 1
            # First slot is after second slot
            elif start_1 > end_2:
                j += 1
            # Slots overlap
            else:
                overlap_start = max(start_1, start_2)
                overlap_end = min(end_1, end_2)
                if overlap_start + duration <= overlap_end:
                    return [overlap_start, overlap_start + duration]
                elif end_1 < end_2:
                    i += 1
                else:
                    j += 1
        return []
