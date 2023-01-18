class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Get number of unique active users for each minute
        minute_to_id = defaultdict(set)
        for id, time in logs:
            minute_to_id[time].add(id)

        # Count active minutes per user across all minutes
        id_to_uam = defaultdict(int)
        for minute, id_set in minute_to_id.items():
            for id in id_set:
                id_to_uam[id] += 1
        
        # Count number of users with active minutes == j
        uam = [0] * k
        for id, minutes in id_to_uam.items():
            uam[minutes-1] += 1
        return uam