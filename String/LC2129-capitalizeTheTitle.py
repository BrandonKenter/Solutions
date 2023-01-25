class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title, res = title.split(), []
        for word in title:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                word = word.lower()
                res.append(word[0].upper() + word[1:])
        return " ".join(res)