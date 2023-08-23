class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        maxi = 0
        used_mentors = [False for i in range(len(mentors))]

        def backtrack(i, cur_total):
            nonlocal maxi
            if i == len(students):
                maxi = max(maxi, cur_total)
                return
            
            for j in range(len(mentors)):
                if used_mentors[j] != True:
                    # choice to use j
                    use_score = self.use_pair(students, mentors, i, j)
                    used_mentors[j] = True
                    backtrack(i + 1, cur_total + use_score)
                    # choice to not use j
                    used_mentors[j] = False
        
        backtrack(0, 0)
        return maxi

    def use_pair(self, students, mentors, i, j):
        score = 0
        for k in range(len(students[i])):
            if students[i][k] == mentors[j][k]:
                score += 1
        return score
            