class Solution:
    def minNumberOfHours(self, initial_energy: int, initial_experience: int, energy: List[int], experience: List[int]) -> int:
        min_energy_dif = min_experience_dif = float('inf')
        cur_energy, cur_experience = initial_energy, initial_experience
        for i in range(len(energy)):
            min_energy_dif = min(min_energy_dif, cur_energy - energy[i] - 1)
            min_experience_dif = min(min_experience_dif, cur_experience - experience[i] - 1)
            cur_energy -= energy[i]
            cur_experience += experience[i]

        t = 0
        if min_energy_dif < 0: t += abs(min_energy_dif)
        if min_experience_dif < 0: t += abs(min_experience_dif) 
        return t
    