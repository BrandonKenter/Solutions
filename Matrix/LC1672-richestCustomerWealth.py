class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for person in accounts:
            person_wealth = 0
            for account in person:
                person_wealth += account
            max_wealth = max(max_wealth, person_wealth)
        return max_wealth
    