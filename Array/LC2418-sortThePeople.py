class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [(h, n) for h, n in zip(heights, names)]
        people.sort(reverse=True)
        return [name for height, name in people]