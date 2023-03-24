class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        rounds = set()
        day_minutes = self.get_minutes("23:59")
        for i in range(0, day_minutes + 1, 15):
            if i <= day_minutes: rounds.add(i)
        
        login_minutes, logout_minutes = self.get_minutes(loginTime), self.get_minutes(logoutTime)
        count = 0
        if login_minutes > logout_minutes:
            for i in range(login_minutes, day_minutes):
                if i in rounds:
                    count += 1
            for i in range(0, logout_minutes):
                if i in rounds and i + 15 <= logout_minutes:
                    count += 1
        else:
            for i in range(login_minutes, logout_minutes):
                if i in rounds and i + 15 <= logout_minutes:
                    count += 1
        return count

    def get_minutes(self, time):
        hours, minutes = time.split(":")
        total = int(hours) * 60 + int(minutes)
        return total
