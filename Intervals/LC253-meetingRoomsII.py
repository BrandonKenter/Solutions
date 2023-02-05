class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        rooms = max_rooms = start_i = end_i = 0
        while start_i < len(starts):
            if starts[start_i] < ends[end_i]: 
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_i += 1
            else:
                rooms -= 1
                end_i += 1
        return max_rooms